#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from com2009_team65_2025.action import ExploreForward

class ExploreForwardServer(Node):

    def __init__(self):
        super().__init__("explore_forward_server")

        self.posx = 0.0
        self.posy = 0.0
        self.lidar_reading = 0.0
        self.shutdown = False

        self.vel_pub = self.create_publisher(Twist, "/cmd_vel", 10)
        self.lidar_sub = self.create_subscription(LaserScan, "/scan", self.lidar_callback, 10)

        self.action_server = ActionServer(
            node=self,
            action_type=ExploreForward,
            action_name="explore_forward",
            execute_callback=self.execute_callback
        )

    def lidar_callback(self, msg):
        # Get the average distance from the front-facing LiDAR sensors
        front_ranges = msg.ranges[:20] + msg.ranges[-20:]
        self.lidar_reading = min(front_ranges)  # Closest obstacle in front

    def execute_callback(self, goal_handle):
        result = ExploreForward.Result()
        feedback = ExploreForward.Feedback()

        fwd_velocity = goal_handle.request.fwd_velocity
        stopping_distance = goal_handle.request.stopping_distance

        self.get_logger().info(f"Starting exploration with velocity {fwd_velocity} m/s.")

        cmd_vel = Twist()
        cmd_vel.linear.x = fwd_velocity

        total_distance = 0.0
        while self.lidar_reading > stopping_distance:
            self.vel_pub.publish(cmd_vel)
            total_distance += fwd_velocity / 10  # Approximate distance per iteration
            feedback.current_distance_to_obstacle = self.lidar_reading
            goal_handle.publish_feedback(feedback)

        self.vel_pub.publish(Twist())  # Stop robot
        result.total_distance_travelled = total_distance

        self.get_logger().info(f"Exploration finished, total distance: {total_distance:.2f} meters.")

        return result

def main(args=None):
    rclpy.init(args=args)
    server = ExploreForwardServer()

    executor = MultiThreadedExecutor()
    executor.add_node(server)

    try:
        executor.spin()
    finally:
        server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
