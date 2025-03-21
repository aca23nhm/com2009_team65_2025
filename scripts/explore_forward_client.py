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
        
        # Define outer zones of the 4x4 arena - this matches the server's zone mapping
        self.outer_zones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]  # All zones on the perimeter
        
    def send_goal(self):
        """Send exploration goal to visit all outer zones efficiently"""
        # Wait for server to be available
        self.get_logger().info('Waiting for exploration action server...')
        self._action_client.wait_for_server()
        
        # Create goal message
        goal_msg = ExploreForward.Goal()
        goal_msg.exploration_time = 120.0  # Increased time for thorough exploration
        
        # Set the goal to visit the outer zones
        self.get_logger().info('Sending exploration goal: Visit all outer zones efficiently')
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
        self.get_logger().info(f'Total zones visited: {result.zones_visited}')
        
        # Calculate exploration efficiency
        efficiency = result.zones_visited / result.total_time
        self.get_logger().info(f'Exploration efficiency: {efficiency:.4f} zones/second')
        
        # Shutdown after receiving result
        rclpy.shutdown()
    
    def feedback_callback(self, feedback_msg):
        """Callback for feedback during exploration"""
        feedback = feedback_msg.feedback
        progress = (feedback.current_zones / 12) * 100  # Assuming 12 total zones
        
        self.get_logger().info(f'Feedback: Time: {feedback.time_elapsed:.2f}s, '
                              f'Zones: {feedback.current_zones}/12 ({progress:.1f}%), '
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
