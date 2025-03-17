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

        self.MIN_DISTANCE = 0.6
        self.ANG_VEL = 0.4

        self.turn_duration = 0.0
        self.turn_start_time = 0.0
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        
        self.ARENA_SIZE = 4.0
        self.ZONE_SIZE = 1.0
        
        self.scan_received = False
        
        self.get_logger().info('Exploration Action Server is ready!')

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        
        zone_x = max(0, min(3, int((self.current_x + self.ARENA_SIZE / 2) // self.ZONE_SIZE)))
        zone_y = max(0, min(3, int((self.current_y + self.ARENA_SIZE / 2) // self.ZONE_SIZE)))
        
        if zone_x in {0, 3} or zone_y in {0, 3}:
            self.zones_visited.add((zone_x, zone_y))
            #self.get_logger().info(f'Visited outer zone: ({zone_x}, {zone_y})') 

    def laser_callback(self, msg):
        self.scan_received = True
        # create segments, a list of 20 degree slices of our environment
        self.segments = []
        for angle in range(359, 0, -20): # count backwards so we scan clockwise
            self.segments.append(
                min([msg.ranges[i] for i in range(angle-19, angle) if not math.isnan(msg.ranges[i])], default=math.inf)
            )
        
        self.obstacles : list = list(map(lambda x: x < self.MIN_DISTANCE, self.segments)) # can we be smarter about minimum distance i.e. can it fit at the given distance?
        self.update_movement_state()
    
    def angle_to_index(self, angles, msg):
        return [int((math.radians(angle) - msg.angle_min) / msg.angle_increment) for angle in angles if 0 <= int((math.radians(angle) - msg.angle_min) / msg.angle_increment) < len(msg.ranges)]
    
    def is_front_obstacle(self): # is there an obstacle in the front 40 degrees?
        return self.obstacles[0] or self.obstacles[17] # again we can maybe smarten this up to allow the robot to slip through smaller gaps.

    def find_direction_to_turn_to(self):
        angle = None
        for i in range(len(self.obstacles)):
            if not self.obstacles[i]: # currently we just take the first clear direction. we could rewrite this to bias
                angle = i * 20 + 10   # towards a region we haven't visited yet.
                break
        if angle is None:
            self.get_logger().fatal("There is no clear way for us to turn!!!")
        return angle
    
    def update_movement_state(self):
        if self.is_front_obstacle() and not self.turn:
            self.move_forward = False
            self.turn = True
            
            # we can definitely save time by changing the direction we rotate.
            self.turn_start_time = time.time()
            deg_to_turn = self.find_direction_to_turn_to()
            time_to_turn = math.radians(deg_to_turn) / self.ANG_VEL
            self.turn_duration = time_to_turn # ang_vel = radians/seconds => seconds = radians / ang_vel

            self.get_logger().info(f"Turning {deg_to_turn}° - turning for {time_to_turn} seconds to achieve this")
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
        fwd_vel = 0.4
        
        if self.turn:
            vel_cmd.linear.x, vel_cmd.angular.z = 0.0, self.ANG_VEL if not self.turn_clockwise else -self.ANG_VEL
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