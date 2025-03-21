#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.qos import qos_profile_sensor_data

from com2009_team65_2025.action import ExploreForward
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

import math
import random
import time

class ExploreForwardServer(Node):
    def __init__(self):
        super().__init__('exploration_action_server')
        
        self.callback_group = ReentrantCallbackGroup()
        
        self._action_server = ActionServer(
            self,
            ExploreForward,
            'exploration',
            self.execute_callback,
            callback_group=self.callback_group
        )
        
        self.vel_pub = self.create_publisher(Twist, 'cmd_vel', 10)
        
        self.laser_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.laser_callback,
            qos_profile_sensor_data,
            callback_group=self.callback_group
        )
        
        self.odom_sub = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10,
            callback_group=self.callback_group
        )
        
        self.min_distance = 0.6
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        
        self.arena_size = 4.0
        self.zone_size = 1.0
        
        self.state = "moving_forward"
        self.turn_start_time = 0.0
        self.turn_duration = 0.0
        self.control_loop_dt = 0.1  # Adjust based on your loop frequency
        self.distance_traveled = 0  # Initialize distance tracking

        
        self.scan_received = False
        
        self.get_logger().info('Exploration Action Server is ready!')

    def laser_callback(self, msg):
        self.scan_received = True

        # Extract front, left, and right ranges
        front_ranges = [msg.ranges[i] for i in self.angle_to_index(range(-30, 31), msg) 
                        if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]
        left_ranges = [msg.ranges[i] for i in self.angle_to_index(range(50, 91), msg) 
                    if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]
        right_ranges = [msg.ranges[i] for i in self.angle_to_index(range(-90, -49), msg) 
                        if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]

        # Determine if obstacles are present
        front_obstacle = min(front_ranges, default=10.0) <= self.min_distance
        left_obstacle = min(left_ranges, default=10.0) <= self.min_distance
        right_obstacle = min(right_ranges, default=10.0) <= self.min_distance

        # Check if we can accelerate (no obstacles within 2m)
        clear_path_ahead = min(front_ranges, default=10.0) > 2.0

        if front_obstacle:
            self.state = "turning"
            self.turn_start_time = time.time()
            self.turn_duration = 1.0
            self.turn_clockwise = left_obstacle or (not left_obstacle and right_obstacle)
            self.distance_traveled = 0  # Reset travel tracker when turning
        
        elif self.state == "turning" and (time.time() - self.turn_start_time > self.turn_duration):
            self.state = "moving_forward"
            self.distance_traveled = 0  # Reset distance when starting forward motion

        # Adjust velocity based on obstacle clearance and distance traveled
        if self.state == "moving_forward":
            if clear_path_ahead and self.distance_traveled < 1.5:
                self.fwd_velocity = 0.5  # Accelerate
                self.distance_traveled += self.fwd_velocity * self.control_loop_dt  # Track distance
                self.get_logger().info(f'accelerating')
            else:
                self.fwd_velocity = 0.2  # Slow down after 1.5m or if an obstacle is detected

    
    def angle_to_index(self, angles, msg):
        return [int((math.radians(angle) - msg.angle_min) / msg.angle_increment) 
        for angle in angles 
        if 0 <= int((math.radians(angle) - msg.angle_min) / msg.angle_increment) < len(msg.ranges)]
    
    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        
        # Determine the zone based on the robot's position
        zone_x = int((self.current_x + self.arena_size / 2) // self.zone_size)
        zone_y = int((self.current_y + self.arena_size / 2) // self.zone_size)
        
        # Ensure the zone is within bounds
        zone_x = max(0, min(3, zone_x))
        zone_y = max(0, min(3, zone_y))
        
        # If any part of the robot is inside an outer zone, mark it as visited
        if (zone_x in {0, 3} or zone_y in {0, 3}) and (zone_x, zone_y) not in self.zones_visited:
            self.zones_visited.add((zone_x, zone_y))
            self.get_logger().info(f'Visited outer zone: ({zone_x}, {zone_y})')

    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing exploration...')
        exploration_time = goal_handle.request.exploration_time
        feedback_msg = ExploreForward.Feedback()
        result = ExploreForward.Result()
        
        self.zones_visited.clear()
        start_time = time.time()
        
        while not self.scan_received and time.time() - start_time < 5.0:
            self.send_velocity_commands()
            time.sleep(0.1)
        
        while (time.time() - start_time) < exploration_time:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Exploration goal canceled')
                self.stop_robot()
                return result
            
            self.send_velocity_commands()
            feedback_msg.time_elapsed = time.time() - start_time
            feedback_msg.current_zones = len(self.zones_visited)
            feedback_msg.current_state = self.state
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.1)
        
        self.stop_robot()
        result.total_time = exploration_time
        result.zones_visited = len(self.zones_visited)
        goal_handle.succeed()
        self.get_logger().info(f'Exploration completed! Visited {len(self.zones_visited)} zones')
        return result
    
    def send_velocity_commands(self):
        vel_cmd = Twist()
        fwd_vel, ang_vel = 0.5, 0.5
        
        if self.state == "turning":
            vel_cmd.linear.x = -0.05
            vel_cmd.angular.z = -ang_vel if self.turn_clockwise else ang_vel
        else:
            vel_cmd.linear.x = fwd_vel
        
        self.vel_pub.publish(vel_cmd)
    
    def stop_robot(self):
        self.vel_pub.publish(Twist())


def main(args=None):
    rclpy.init(args=args)
    exploration_server = ExploreForwardServer()
    executor = MultiThreadedExecutor()
    executor.add_node(exploration_server)
    try:
        executor.spin()
    except KeyboardInterrupt:
        pass
    finally:
        exploration_server.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()