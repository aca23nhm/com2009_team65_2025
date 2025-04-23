#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, PoseStamped
from std_msgs.msg import Bool
import time

class ExplorationController(Node):
    def __init__(self):
        super().__init__("exploration_controller")

        # Publishers and subscribers
        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.scan_subscriber = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.pose_subscriber = self.create_subscription(PoseStamped, '/robot_pose', self.pose_callback, 10)
        self.done_publisher = self.create_publisher(Bool, '/exploration_done', 10)

        # Zone tracking
        self.visited_zones = set()
        self.time_start = time.time()
        self.exploration_finished = False

        self.zones = [
            [(0, 0), (1, 1)], [(1, 0), (2, 1)], [(2, 0), (3, 1)],
            [(0, 1), (1, 2)], [(1, 1), (2, 2)], [(2, 1), (3, 2)],
            [(0, 2), (1, 3)], [(1, 2), (2, 3)], [(2, 2), (3, 3)]
        ]
        self.total_zones = len(self.zones)

        self.twist = Twist()

        self.get_logger().info("Exploration Controller started.")

    def pose_callback(self, msg):
        if self.exploration_finished:
            return

        x, y = msg.pose.position.x, msg.pose.position.y
        self.get_logger().info(f"Robot Position: x={x:.2f}, y={y:.2f}")

        for i, zone in enumerate(self.zones):
            (x_min, y_min), (x_max, y_max) = zone
            if x_min <= x <= x_max and y_min <= y <= y_max:
                if i not in self.visited_zones:
                    self.visited_zones.add(i)
                    self.get_logger().info(f"Entered zone {i+1}/{self.total_zones}. Visited: {len(self.visited_zones)}/{self.total_zones}")
                    
                    if len(self.visited_zones) == self.total_zones:
                        self.get_logger().info("✅ All zones visited.")
                        self.stop_robot()
                break

    def scan_callback(self, msg):
        if self.exploration_finished:
            return

        if time.time() - self.time_start > 180:
            self.get_logger().info("⏳ Time limit reached.")
            self.stop_robot()
            return

        min_distance = min(msg.ranges[0:20] + msg.ranges[-20:])
        self.get_logger().info(f"Min Distance: {min_distance:.2f}")

        if min_distance < 0.7:
            self.avoid_obstacle()
        else:
            self.move_forward()

    def avoid_obstacle(self):
        self.get_logger().info("🚧 Obstacle detected. Rotating...")
        self.twist.linear.x = -0.01
        self.twist.angular.z = 0.6
        self.publisher.publish(self.twist)

    def move_forward(self):
        self.get_logger().info("🚗 Moving forward...")
        self.twist.linear.x = 0.26
        self.twist.angular.z = 0.0
        self.publisher.publish(self.twist)

    def stop_robot(self):
        if not self.exploration_finished:
            self.get_logger().info("🛑 Stopping robot and publishing /exploration_done.")
            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.publisher.publish(self.twist)

            # ✅ Publish the exploration_done message
            done_msg = Bool()
            done_msg.data = True
            self.done_publisher.publish(done_msg)

            self.exploration_finished = True

def main(args=None):
    rclpy.init(args=args)
    controller = ExplorationController()
    rclpy.spin(controller)
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
