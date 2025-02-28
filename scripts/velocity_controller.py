#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
import math
import signal
import sys

class VelocityController(Node):
    def __init__(self):
        super().__init__('velocity_controller')

        # Publisher for velocity commands
        self.vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Subscriber for odometry
        self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

        # Timer to print odometry data at 1Hz
        self.create_timer(1.0, self.print_odometry)

        # Motion parameters
        self.radius = 0.5  # 1m diameter = 0.5m radius
        self.linear_speed = (2 * math.pi * self.radius) / 27.0  # Complete full circle in 30 seconds
        self.angular_speed = self.linear_speed / self.radius  # ω = v/r

        # Motion tracking
        self.x_start, self.y_start = None, None  # Store initial position
        self.yaw_start = None  # Store initial yaw
        self.yaw_accumulated = 0.0  # Track cumulative yaw change
        self.phase = "loop1"  # Start with the first loop

        # Timer to publish velocity commands
        self.timer = self.create_timer(0.1, self.run_motion)

        self.get_logger().info("Starting figure-eight movement...")

        # Handle SIGINT (Ctrl + C) to stop the robot
        signal.signal(signal.SIGINT, self.shutdown)

    def odom_callback(self, msg):
        """ Callback to get odometry data """
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        _, _, current_yaw = self.get_euler_from_quaternion(msg.pose.pose.orientation)

        # Store initial values once
        if self.x_start is None or self.y_start is None or self.yaw_start is None:
            self.x_start, self.y_start, self.yaw_start = self.current_x, self.current_y, current_yaw

        # Track cumulative yaw change
        yaw_diff = self.angle_difference(current_yaw, self.yaw_start)
        self.yaw_accumulated += yaw_diff
        self.yaw_start = current_yaw  # Update yaw reference

        self.current_yaw = current_yaw  # Store for logging

    def print_odometry(self):
        """ Print odometry data to terminal every second """
        if hasattr(self, "current_x"):
            self.get_logger().info(
                f"x={self.current_x:.2f} [m], y={self.current_y:.2f} [m], yaw={math.degrees(self.current_yaw):.1f} [degrees]"
            )

    def run_motion(self):
        """ Publish velocity commands to make full circles before switching loops """
        if self.x_start is None or self.y_start is None or self.yaw_start is None:
            return  # Wait until odometry data is received

        twist = Twist()

        if self.phase == "loop1":
            twist.linear.x = self.linear_speed
            twist.angular.z = self.angular_speed  # Counterclockwise motion

            # Switch to loop2 when the robot completes a full 360-degree turn
            if abs(self.yaw_accumulated) >= 2 * math.pi - 0.14:  # 360 degrees in radians
                self.phase = "loop2"
                self.yaw_accumulated = 0.0  # Reset accumulated yaw
                self.get_logger().info("Switching to second loop (clockwise)")

        elif self.phase == "loop2":
            twist.linear.x = self.linear_speed
            twist.angular.z = -self.angular_speed  # Clockwise motion

            # Stop when the second full circle is completed
            if abs(self.yaw_accumulated) >= 2 * math.pi:  # Another 360-degree turn
                self.phase = "stop"

        if self.phase == "stop":
            twist.linear.x = 0.0
            twist.angular.z = 0.0
            self.vel_pub.publish(twist)
            self.get_logger().info("Stopping movement. Figure-eight complete!")
            self.destroy_node()
            return

        self.vel_pub.publish(twist)

    def shutdown(self, signum, frame):
        """ Stop the robot safely when Ctrl+C is pressed """
        self.get_logger().info("Shutting down, stopping robot...")
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.vel_pub.publish(twist)
        self.destroy_node()
        rclpy.shutdown()
        sys.exit(0)

    def get_euler_from_quaternion(self, quat):
        """ Convert quaternion to Euler angles """
        x, y, z, w = quat.x, quat.y, quat.z, quat.w
        sinr_cosp = 2 * (w * x + y * z)
        cosr_cosp = 1 - 2 * (x * x + y * y)
        roll = math.atan2(sinr_cosp, cosr_cosp)
        sinp = 2 * (w * y - z * x)
        pitch = math.asin(sinp) if abs(sinp) <= 1 else math.copysign(math.pi / 2, sinp)
        siny_cosp = 2 * (w * z + x * y)
        cosy_cosp = 1 - 2 * (y * y + z * z)
        yaw = math.atan2(siny_cosp, cosy_cosp)
        return roll, pitch, yaw

    def angle_difference(self, new_angle, old_angle):
        """ Compute the smallest difference between two angles in radians """
        diff = new_angle - old_angle
        while diff > math.pi:
            diff -= 2 * math.pi
        while diff < -math.pi:
            diff += 2 * math.pi
        return diff

def main(args=None):
    rclpy.init(args=args)
    node = VelocityController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
