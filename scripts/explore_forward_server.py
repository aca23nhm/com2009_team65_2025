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
        
        self.move_forward = True
        self.turn = False
        self.turn_clockwise = False
        self.stop = False
        
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
        
        self.front_obstacle = False
        self.left_obstacle = False
        self.right_obstacle = False
        self.min_distance = 0.6
        self.turn_duration = 0.0
        self.turn_start_time = 0.0
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        
        self.arena_size = 4.0
        self.zone_size = 1.0
        
        self.scan_received = False
        
        self.get_logger().info('Exploration Action Server is ready!')

    def laser_callback(self, msg):
        self.scan_received = True
        front_ranges = [msg.ranges[i] for i in self.angle_to_index(range(-20, 21), msg) if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]
        left_ranges = [msg.ranges[i] for i in self.angle_to_index(range(50, 91), msg) if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]
        right_ranges = [msg.ranges[i] for i in self.angle_to_index(range(-90, -49), msg) if not math.isnan(msg.ranges[i]) and not math.isinf(msg.ranges[i])]
        
        self.front_obstacle = min(front_ranges, default=10.0) < self.min_distance
        self.left_obstacle = min(left_ranges, default=10.0) < self.min_distance
        self.right_obstacle = min(right_ranges, default=10.0) < self.min_distance
        
        self.update_movement_state()
    
    def angle_to_index(self, angles, msg):
        return [int((math.radians(angle) - msg.angle_min) / msg.angle_increment) for angle in angles if 0 <= int((math.radians(angle) - msg.angle_min) / msg.angle_increment) < len(msg.ranges)]
    
    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        
        zone_x = max(0, min(3, int((self.current_x + self.arena_size / 2) // self.zone_size)))
        zone_y = max(0, min(3, int((self.current_y + self.arena_size / 2) // self.zone_size)))
        
        if zone_x in {0, 3} or zone_y in {0, 3}:
            self.zones_visited.add((zone_x, zone_y))
            self.get_logger().info(f'Visited outer zone: ({zone_x}, {zone_y})')
    
    def update_movement_state(self):
        if self.front_obstacle:
            self.move_forward = False
            self.turn = True
            self.turn_clockwise = self.left_obstacle
            self.turn_start_time = time.time()
            self.turn_duration = random.uniform(1.0, 2.0)
        elif self.turn and (time.time() - self.turn_start_time > self.turn_duration):
            self.turn = False
            self.move_forward = True
    
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
            feedback_msg.current_state = "turning" if self.turn else "moving forward"
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
        fwd_vel, ang_vel = 0.4, 0.4
        
        if self.turn:
            vel_cmd.linear.x, vel_cmd.angular.z = 0.0, ang_vel if not self.turn_clockwise else -ang_vel
        elif self.move_forward:
            vel_cmd.linear.x, vel_cmd.angular.z = fwd_vel, 0.0
        
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