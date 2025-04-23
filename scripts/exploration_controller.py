#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

class ExplorationController(Node):
    def __init__(self):
        super().__init__("exploration_controller")

        self.publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        self.scan_subscriber = self.create_subscription(LaserScan, '/scan', self.scan_callback, 10)
        self.twist = Twist()
        self.get_logger().info("Exploration Controller started.")

    def scan_callback(self, msg):
        # Get the minimum distance from the LaserScan data (front of the robot)
        min_distance = min(msg.ranges[0:20] + msg.ranges[-20:])
        
        if min_distance < 0.5:  # If an obstacle is too close
            self.avoid_obstacle()
        else:
            self.move_forward()

    def avoid_obstacle(self):
        self.get_logger().info("Obstacle too close, rotating...")
        self.twist.linear.x = 0.0
        self.twist.angular.z = 0.5  # Rotate to avoid the obstacle
        self.publisher.publish(self.twist)

    def move_forward(self):
        self.get_logger().info("Moving forward...")
        self.twist.linear.x = 0.2  # Move at a constant speed
        self.twist.angular.z = 0.0
        self.publisher.publish(self.twist)

def main(args=None):
    rclpy.init(args=args)
    exploration_controller = ExplorationController()
    rclpy.spin(exploration_controller)
    exploration_controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()