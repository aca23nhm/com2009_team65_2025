#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from rclpy.qos import QoSProfile, qos_profile_sensor_data
from rclpy.callback_groups import ReentrantCallbackGroup

import math
import time

class Explorer(Node):
    def __init__(self):
        super().__init__('explorer_node')

        self.callback_group = ReentrantCallbackGroup()

        # Publishers
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)

        # Subscribers
        self.laser_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            qos_profile_sensor_data,
            callback_group=self.callback_group
        )

        # Control loop
        self.control_timer = self.create_timer(0.1, self.control_loop, callback_group=self.callback_group)
        self.start_time = self.get_clock().now()
        self.last_printed_second = -1

        self.MIN_DISTANCE = 0.3  # Threshold for obstacle detection
        self.obstacle_in_front = False
        self.scan_received = False

        self.get_logger().info("Explorer node started. Exploring for 180 seconds.")

    def mean_of_lowest_5(self, arr):
        cleaned = [r for r in arr if not math.isnan(r) and r > 0.01]
        if len(cleaned) < 5:
            return float('inf')
        return sum(sorted(cleaned)[0:5]) / 5

    def laser_callback(self, msg):
        # We'll analyze the front 60 degrees (±30)
        center_index = len(msg.ranges) // 2
        front_ranges = msg.ranges[center_index - 30 : center_index + 30]
        mean_distance = self.mean_of_lowest_5(front_ranges)
        self.obstacle_in_front = mean_distance < self.MIN_DISTANCE
        self.scan_received = True

    def control_loop(self):
        now = self.get_clock().now()
        elapsed = (now - self.start_time).nanoseconds / 1e9
        time_left = 180 - int(elapsed)

        # Print time every second
        if time_left != self.last_printed_second and time_left >= 0:
            self.get_logger().info(f"Time remaining: {time_left} seconds")
            self.last_printed_second = time_left

        if elapsed >= 180.0:
            self.stop_robot()
            self.get_logger().info("⏱️ Time is up! Robot stopped.")
            self.control_timer.cancel()
            return

        # Movement logic
        if not self.scan_received:
            return

        twist = Twist()
        if self.obstacle_in_front:
            # Turn if obstacle ahead
            twist.linear.x = 0.0
            twist.angular.z = 0.5
        else:
            # Move forward with slight curve
            twist.linear.x = 0.15
            twist.angular.z = 0.1

        self.vel_pub.publish(twist)

    def stop_robot(self):
        stop_msg = Twist()
        self.vel_pub.publish(stop_msg)

def main(args=None):
    rclpy.init(args=args)
    node = Explorer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()

