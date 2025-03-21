#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionClient
from rclpy.executors import SingleThreadedExecutor

from com2009_team65_2025.action import ExploreForward

class ExploreServerClient(Node):
    def __init__(self):
        super().__init__('exploration_action_client')
        
        # Create action client
        self._action_client = ActionClient(
            self,
            ExploreForward,
            'exploration'
        )
        
        # Define outer zones of the 4x4 arena
        self.outer_zones = set([
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 0), (1, 3), (2, 0), (2, 3),
            (3, 0), (3, 1), (3, 2), (3, 3)
        ])
    
    def send_goal(self):
        """Send exploration goal to visit all outer zones"""
        # Wait for server to be available
        self.get_logger().info('Waiting for exploration action server...')
        self._action_client.wait_for_server()
        
        # Create goal message
        goal_msg = ExploreForward.Goal()
        goal_msg.exploration_time = 190.0  # Use a fixed time for the exploration
        
        # Set the goal to visit the outer zones
        self.get_logger().info('Sending exploration goal: Visit all outer zones')
        self._send_goal_future = self._action_client.send_goal_async(
            goal_msg,
            feedback_callback=self.feedback_callback
        )
        
        # Add callback for when goal is accepted
        self._send_goal_future.add_done_callback(self.goal_response_callback)
    
    def goal_response_callback(self, future):
        """Callback for when goal is accepted/rejected"""
        goal_handle = future.result()
        
        if not goal_handle.accepted:
            self.get_logger().error('Goal was rejected!')
            return
        
        self.get_logger().info('Goal accepted!')
        
        # Request result
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
    
    def get_result_callback(self, future):
        """Callback for when result is received"""
        result = future.result().result
        self.get_logger().info(f'Exploration completed!')
        self.get_logger().info(f'Time spent: {result.total_time:.2f} seconds')
        self.get_logger().info(f'Zones visited: {result.zones_visited}')
        
        # Shutdown after receiving result
        rclpy.shutdown()
    
    def feedback_callback(self, feedback_msg):
        """Callback for feedback during exploration"""
        feedback = feedback_msg.feedback
        self.get_logger().info(f'Feedback: Time: {feedback.time_elapsed:.2f}s, '
                               f'Zones: {feedback.current_zones}, '
                               f'State: {feedback.current_state}')


def main(args=None):
    rclpy.init(args=args)
    
    # Create client
    action_client = ExploreServerClient()
    
    # Send goal to explore all outer zones
    action_client.send_goal()
    
    # Spin until the action completes
    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
