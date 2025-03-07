#!/usr/bin/env python3

import rclpy
import random
import time
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ObstacleAvoidance(Node):
    def __init__(self):
        super().__init__('obstacle_avoidance')

        # Create subscriber for LiDAR data
        self.lidar_sub = self.create_subscription(LaserScan, '/scan', self.lidar_callback, 10)

        # Create publisher for velocity commands
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        # Movement control variables
        self.safe_distance = 0.5  # Increased for better avoidance
        self.forward_speed = 0.15  # Adjusted for safer movement
        self.turn_speed = 0.5  # Faster turning
        self.backup_speed = -0.1  # Speed when backing up

        # Initialize LiDAR readings
        self.front = float('inf')
        self.left = float('inf')
        self.right = float('inf')

        # Track time for 90-second exploration
        self.start_time = None  # Only starts counting when movement begins

        # Timer for movement control loop
        self.timer = self.create_timer(0.1, self.move_robot)

    def lidar_callback(self, msg):
        """Process LiDAR data and determine obstacle positions"""
        if len(msg.ranges) == 0:
            self.get_logger().warn("LiDAR data is empty!")
            return

        # Extract front, left, and right distances
        self.front = min(min(msg.ranges[0:15] + msg.ranges[-15:]), 10.0)  # Front
        self.left = min(min(msg.ranges[60:120]), 10.0)  # Left
        self.right = min(min(msg.ranges[-120:-60]), 10.0)  # Right

        self.get_logger().info(f"LiDAR: Front={self.front:.2f}, Left={self.left:.2f}, Right={self.right:.2f}")

    def move_robot(self):
        """Control logic for avoiding obstacles and exploring"""

        # Start timer when movement begins
        if self.start_time is None:
            self.start_time = time.time()

        # Stop after 90 seconds
        if time.time() - self.start_time > 90:
            self.get_logger().info("Exploration complete! Stopping robot.")
            self.stop_robot()
            return

        twist = Twist()

        # Ensure LiDAR data is valid before making decisions
        if self.front == float('inf') or self.left == float('inf') or self.right == float('inf'):
            self.get_logger().warn("Waiting for valid LiDAR data...")
            return

        # Obstacle avoidance strategy
        if self.front < self.safe_distance:
            self.get_logger().info("Obstacle ahead! Avoiding...")
            twist.linear.x = self.backup_speed  # Move backward slightly
            twist.angular.z = self.turn_speed if self.left > self.right else -self.turn_speed  # Turn away from obstacle
        elif self.left < self.safe_distance:
            self.get_logger().info("Wall on left! Turning right...")
            twist.linear.x = self.forward_speed
            twist.angular.z = -self.turn_speed
        elif self.right < self.safe_distance:
            self.get_logger().info("Wall on right! Turning left...")
            twist.linear.x = self.forward_speed
            twist.angular.z = self.turn_speed
        else:
            # Move forward but adjust direction occasionally to explore
            twist.linear.x = self.forward_speed
            if random.random() < 0.05:  # Random slight turns to avoid getting stuck
                self.get_logger().info("Random exploration turn...")
                twist.angular.z = random.choice([-self.turn_speed, self.turn_speed])

        self.cmd_vel_pub.publish(twist)

    def stop_robot(self):
        """Stops the robot and shuts down the node"""
        twist = Twist()
        twist.linear.x = 0.0
        twist.angular.z = 0.0
        self.cmd_vel_pub.publish(twist)
        rclpy.shutdown()

def main(args=None):
    rclpy.init(args=args)
    node = ObstacleAvoidance()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
