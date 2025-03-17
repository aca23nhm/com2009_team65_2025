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
        self.ANG_VEL = 0.8

        self.turn_duration = 0.0
        self.turn_start_time = 0.0
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        
        self.ARENA_SIZE = 4.0
        self.ZONE_SIZE = 1.0

        # coordinates, from origin, in metres, of the centres of all of the zones
        # top row + bottom row + sides
        zones : list = [(x/10, 1.5) for x in range(-15, 20, 5)] + [(x/10, -1.5) for x in range(-15, 20, 5) ] + [(-1.5, 0.5), (-1.5, -0.5), (1.5, 0.5), (1.5, -0.5)] # 12, 11, 5, 6
        self.zones_visited = dict(zip(zones, [False] * len(zones))) # dict with zones as keys and bools as values

        self.scan_received = False
        
        self.get_logger().info('Exploration Action Server is ready!')

    def odom_callback(self, msg):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y

        current_square = list(filter(lambda k : is_in_square(
            self.current_x, self.current_y, *k, 1 # the star is an unpacking operator since k is a tuple
        ), self.zones_visited.keys()))
        
        if current_square and not self.zones_visited[current_square]:
            self.get_logger().info(f"We just visited the zone at ({current_square[0]}, {current_square[1]})!")
            self.zones_visited[current_square] = True

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
        return self.obstacles[0] or self.obstacles[-1] # again we can maybe smarten this up to allow the robot to slip through smaller gaps.

    def find_direction_to_turn_to(self):
        angle = None
        for i in range(len(self.obstacles)):
            if not self.obstacles[i]: # currently we just take the first clear direction. we could rewrite this to bias
                angle = i * 20 + 10   # towards a region we haven't visited yet, or even just choose a random
                break
        if angle is None:
            self.get_logger().fatal("There is no clear way for us to turn!!!")
        return angle
    
    def find_direction_to_turn_to_random(self):
        angle = None
        angles = []
        for i in range(len(self.obstacles)):
            if not self.obstacles[i]: 
                angles.append(i)
        angle = (random.choice(angles) * 20 + 10)
        if angle is None:
            self.get_logger().fatal("There is no clear way for us to turn!!!")
        return angle
    
    def tan_angle_to_point(self, x, y): 
        return (x - self.current_x) / (y - self.current_y)

    def find_direction_to_turn_to_zone_based(self):
        unvisited = list(filter(lambda k: not self.zones_visited[k] ,self.zones_visited.keys()))
        unvisited.sort(key=lambda k : self.tan_angle_to_point(*k)) # do we need to arctan this? idr a level geometry :D
        target = unvisited[0]
        angle = math.atan(self.tan_angle_to_point(target[0], target[1]))
        return angle
        

    def update_movement_state(self):
        if self.is_front_obstacle() and not self.turn:
            self.move_forward = False
            self.turn = True
            
            # we can definitely save time by changing the direction we rotate.
            self.turn_start_time = time.time()
            deg_to_turn = self.find_direction_to_turn_to_zone_based()
            time_to_turn = abs(self.find_direction_to_turn_to_zone_based() / self.ANG_VEL)
            self.turn_duration = time_to_turn # ang_vel = radians/seconds => seconds = radians / ang_vel

            self.get_logger().info(f"Turning {deg_to_turn} rads - turning for {time_to_turn} seconds to achieve this")
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
            
            if self.scan_received:
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
            vel_cmd.linear.x, vel_cmd.angular.z = 0.0, self.ANG_VEL 
        elif self.move_forward:
            vel_cmd.linear.x, vel_cmd.angular.z = fwd_vel, 0.0
        
        self.vel_pub.publish(vel_cmd)
    
    def stop_robot(self):
        self.vel_pub.publish(Twist())

# x,y of point, x,y of centre of square, side length of square
def is_in_square(x, y, ox, oy, sl):
    return ox + (sl/2) < x < ox - (sl/2) and oy + (sl/2) < y < oy - (sl/2)

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