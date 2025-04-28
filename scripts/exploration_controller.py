#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist, PoseStamped
from std_msgs.msg import Bool
import time

class ExplorationController(Node):
    def __init__(self):
        super().__init__('exploration_controller')

        # Publishers and Subscribers
        self.cmd_vel_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.scan_sub = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.pose_sub = self.create_subscription(PoseStamped, '/robot_pose', self.pose_callback, 10)
        self.done_pub = self.create_publisher(Bool, '/exploration_done', 10)

        # Initialize variables
        self.visited_zones = set()
        self.time_start = time.time()
        self.exploration_finished = False
        self.twist = Twist()

        # Define 9 zones (3x3 grid)
        self.zones = [
            [(0, 0), (1, 1)], [(1, 0), (2, 1)], [(2, 0), (3, 1)],
            [(0, 1), (1, 2)], [(1, 1), (2, 2)], [(2, 1), (3, 2)],
            [(0, 2), (1, 3)], [(1, 2), (2, 3)], [(2, 2), (3, 3)]
        ]
        self.total_zones = len(self.zones)

        # Threshold for obstacle detection
        self.obstacle_distance_threshold = 0.38

        self.get_logger().info('Exploration Controller node has started.')

    def pose_callback(self, msg):
        if self.exploration_finished:
            return

        x, y = msg.pose.position.x, msg.pose.position.y
        self.get_logger().debug(f'Robot Position: x={x:.2f}, y={y:.2f}')

        for i, ((x_min, y_min), (x_max, y_max)) in enumerate(self.zones):
            if x_min <= x <= x_max and y_min <= y <= y_max:
                if i not in self.visited_zones:
                    self.visited_zones.add(i)
                    self.get_logger().info(f'Entered Zone {i+1}/{self.total_zones}. Zones Visited: {len(self.visited_zones)}/{self.total_zones}')
                    
                    if len(self.visited_zones) == self.total_zones:
                        self.get_logger().info('All zones visited!')
                        self.stop_robot()
                break

    def scan_callback(self, msg):
        if self.exploration_finished:
            return

        elapsed_time = time.time() - self.time_start
        if elapsed_time > 180:
            self.get_logger().info('180 seconds elapsed. Stopping exploration.')
            self.stop_robot()
            return

        ranges = msg.ranges
        num_ranges = len(ranges)

        # Properly divide left and right
        left = ranges[num_ranges//2 : num_ranges]
        right = ranges[0 : num_ranges//2]

        # Filter invalid readings
        left = [r for r in left if 0.05 < r < 3.5]
        right = [r for r in right if 0.05 < r < 3.5]

        min_left = min(left) if left else float('inf')
        min_right = min(right) if right else float('inf')
        min_front = min(ranges[-10:] + ranges[:10]) if ranges else float('inf')  # ±10°

        self.get_logger().debug(f"Min Front: {min_front:.2f}, Min Left: {min_left:.2f}, Min Right: {min_right:.2f}")

        if min_front < self.obstacle_distance_threshold:
            self.avoid_obstacle(min_left, min_right)
        else:
            self.move_forward()

    def move_forward(self):
        self.get_logger().debug('🚗 Moving forward.')
        self.twist.linear.x = 0.26
        self.twist.angular.z = 0.0
        self.cmd_vel_pub.publish(self.twist)

    def avoid_obstacle(self, min_left, min_right):
        self.get_logger().info('🚧 Obstacle detected. Deciding turn direction.')

        self.twist.linear.x = 0.0  # Stop forward motion first

        if min_left > min_right:
            # More space on left, turn left
            self.twist.angular.z = 0.6
            self.get_logger().info('Turning left to avoid obstacle.')
        else:
            # More space on right, turn right
            self.twist.angular.z = -0.6
            self.get_logger().info('Turning right to avoid obstacle.')

        self.cmd_vel_pub.publish(self.twist)

    def stop_robot(self):
        if not self.exploration_finished:
            self.exploration_finished = True
            self.get_logger().info('🛑 Stopping robot and publishing /exploration_done.')

            self.twist.linear.x = 0.0
            self.twist.angular.z = 0.0
            self.cmd_vel_pub.publish(self.twist)

            done_msg = Bool()
            done_msg.data = True
            self.done_pub.publish(done_msg)

    def destroy_node(self):
        self.get_logger().info('Shutting down Exploration Controller node.')
        super().destroy_node()

def main(args=None):
    rclpy.init(args=args)
    node = ExplorationController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
