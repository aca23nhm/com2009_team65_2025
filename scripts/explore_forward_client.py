#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from geometry_msgs.msg import Twist
from com2009_team65_2025.action import ExploreForward

class ExploreForwardClient(Node):

    def __init__(self):
        super().__init__("explore_forward_client")
        self.action_client = ActionClient(self, ExploreForward, "explore_forward")

    def send_goal(self, fwd_velocity=0.2, stopping_distance=0.5):
        goal_msg = ExploreForward.Goal()
        goal_msg.fwd_velocity = fwd_velocity
        goal_msg.stopping_distance = stopping_distance

        self.get_logger().info(f"Sending goal to explore with velocity: {fwd_velocity} m/s, stop distance: {stopping_distance} m.")

        self.action_client.wait_for_server()
        send_goal_future = self.action_client.send_goal_async(goal_msg)
        send_goal_future.add_done_callback(self.goal_response_callback)

    def goal_response_callback(self, future):
        goal_handle = future.result()
        if not goal_handle.accepted:
            self.get_logger().info("Goal rejected.")
            return

        self.get_logger().info("Goal accepted, waiting for result...")
        result_future = goal_handle.get_result_async()
        result_future.add_done_callback(self.result_callback)

    def result_callback(self, future):
        result = future.result().result
        self.get_logger().info(f"Exploration completed, total distance travelled: {result.total_distance_travelled:.2f} meters.")

def main(args=None):
    rclpy.init(args=args)
    client = ExploreForwardClient()

    try:
        client.send_goal()
        rclpy.spin(client)
    except KeyboardInterrupt:
        client.get_logger().info("Exploration stopped.")
    finally:
        client.destroy_node()
        rclpy.shutdown()

if __name__ == "__main__":
    main()
