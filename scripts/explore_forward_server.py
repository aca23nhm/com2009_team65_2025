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

from itertools import takewhile, dropwhile

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
        self.MINIMUM_SAFE_TURN = math.radians(20)
        self.ANG_VEL = 0.8

        self.turn_duration = 0.0
        self.turn_start_time = 0.0
        self.clockwise = True
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        
        self.ARENA_SIZE = 4.0
        self.ZONE_SIZE = 1.0
        
        # coordinates, from origin, in metres, of the centres of all of the zones
        # top row + bottom row + sides   1 2 3 4                      5              6                   7  8  9  10                                11          12   
        zones : list = [(-1.5, y/10) for y in range(-15, 20, 10)] + [(-0.5, 1.5), (0.5, 1.5)] + [(1.5, y/10) for y in range(15, -20, -10) ] + [(0.5, -1.5), (-0.5, -1.5)]
        self.zones_visited = dict(zip(zones, [False] * len(zones))) # dict with zones as keys and bools as values
        self.get_logger().info(f"self.zones_visited is initialised as {self.zones_visited}")

        self.scan_received = False
        
        self.get_logger().info('Exploration Action Server is ready!')

    def odom_callback(self, msg : Odometry):
        self.current_x = msg.pose.pose.position.x
        self.current_y = msg.pose.pose.position.y
        _, _, self.current_yaw = get_euler_from_quaternion(msg.pose.pose.orientation)

        current_square = list(filter(lambda k : is_in_circle( # using the circle instead of the square to make sure we fully enter the square
            self.current_x, self.current_y, *k, 0.5 # the star is an unpacking operator since k is a tuple
        ), self.zones_visited.keys()))

        if current_square != [] and not self.zones_visited[current_square[0]]:
            current_square = current_square[0]
            self.get_logger().info(f"We just visited Zone {self.zone_at_coords((current_square[0], current_square[1]))}!")
            self.zones_visited[current_square] = True

    def laser_callback(self, msg):
        # create segments, a list of 20 degree slices of our environment
        self.segments = []
        for angle in range(359, 0, -20): # count backwards so we scan clockwise
            self.segments.append(
                min([msg.ranges[i] for i in range(angle-19, angle) if not math.isnan(msg.ranges[i])], default=math.inf)
            )
        
        self.obstacles : list = list(map(lambda x: x < self.MIN_DISTANCE, self.segments)) # can we be smarter about minimum distance i.e. can it fit at the given distance?
        self.update_movement_state()
        self.scan_received = True
    
    def zone_at_coords(self, coords):
        return list(self.zones_visited.keys()).index(coords) + 1

    def angle_to_index(self, angles, msg):
        return [int((math.radians(angle) - msg.angle_min) / msg.angle_increment) for angle in angles if 0 <= int((math.radians(angle) - msg.angle_min) / msg.angle_increment) < len(msg.ranges)]
    
    def is_front_obstacle(self): # is there an obstacle in the front 40 degrees?
        return self.obstacles[0] or self.obstacles[-1] # again we can maybe smarten this up to allow the robot to slip through smaller gaps.

    # find the dot product of the vector from the robot to the point, and the unit vector of our current orientation
    def cos_angle_to_point(self, target_x, target_y):
        delta_x = target_x - self.current_x
        delta_y = target_y - self.current_y
        dot_prod = delta_x * math.cos(self.current_yaw) + delta_y * math.sin(self.current_yaw)
        cos_th = dot_prod / math.sqrt( # cosθ = a · b / |a||b|, and sin²θ + cos²θ = 1
            math.pow(delta_x, 2) + math.pow(delta_y, 2))
        return cos_th

    def find_direction_to_turn_to(self):
        angle = None
        for i in range(len(self.obstacles)):
            if not self.obstacles[i]:   
                angle = i * 20 + 10   
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
        return (y - self.current_y) / (x - self.current_x)

    def find_direction_to_turn_to_zone_based(self):

        point_to_angle = lambda k : abs(math.acos(self.cos_angle_to_point(*k)))

        unvisited = list(filter(lambda k: not self.zones_visited[k] ,self.zones_visited.keys()))
        unvisited.sort(key=point_to_angle) # abs it so the shortest turn (otherwise it will always turn the negativest)

        unsafe = list(takewhile(lambda p: point_to_angle(p) < self.MINIMUM_SAFE_TURN, unvisited))
        safe = list(dropwhile(lambda p: point_to_angle(p) < self.MINIMUM_SAFE_TURN, unvisited))
        self.get_logger().info(f"Safe turns: {list(map(self.zone_at_coords, safe))}, unsafe turns: {list(map(self.zone_at_coords, unsafe))}")
        if any(safe):
            target = (safe)[0] if point_to_angle(safe[0]) < self.MINIMUM_SAFE_TURN * 2.5 else None
        else:
            target = (unsafe)[-1] # maybe clamp to 20? we'll see
        
        if target is not None:
            self.get_logger().info(f"We are turning towards Zone {self.zone_at_coords(target)}")
            self.get_logger().info(f"Current Yaw: {math.degrees(self.current_yaw)}, origin-point angle: {math.degrees(self.tan_angle_to_point(target[0], target[1]))}")
            angle = math.acos(self.cos_angle_to_point(target[0], target[1])) 
        else:
            self.get_logger().info("Making minimum safe turn")
            angle = math.copysign(self.MINIMUM_SAFE_TURN, point_to_angle(safe[0]))
        self.turn_clockwise = angle > 0
        return angle
    

    def update_movement_state(self):
        if self.is_front_obstacle() and not self.turn:
            self.move_forward = False
            self.turn = True
            
            # we can definitely save time by changing the direction we rotate.
            self.turn_start_time = time.time()
            turn_angle = clamp_turn_angle(self.find_direction_to_turn_to_zone_based()) # remember to reclamp!!!!
            time_to_turn = abs(turn_angle / self.ANG_VEL)
            self.turn_duration = time_to_turn # ang_vel = radians/seconds => seconds = radians / ang_vel

            self.get_logger().info(f"Turning {math.degrees(turn_angle)}° - turning for {time_to_turn} seconds {'anti' if not self.turn_clockwise else ''}clockwise to achieve this")
        elif self.turn and (time.time() - self.turn_start_time > self.turn_duration):
            self.turn = False
            self.move_forward = True
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing exploration...')
        exploration_time = goal_handle.request.exploration_time
        feedback_msg = ExploreForward.Feedback()
        result = ExploreForward.Result()
        
        start_time = time.time()
        
        # reinitialise zones_visited
        # coordinates, from origin, in metres, of the centres of all of the zones
        # top row + bottom row + sides   1 2 3 4                      5              6                   7  8  9  10                                11          12   
        zones : list = [(-1.5, y/10) for y in range(-15, 20, 10)] + [(-0.5, 1.5), (0.5, 1.5)] + [(1.5, y/10) for y in range(15, -20, -10) ] + [(0.5, -1.5), (-0.5, -1.5)]
        self.zones_visited = dict(zip(zones, [False] * len(zones))) # dict with zones as keys and bools as values

        while not self.scan_received and time.time() - start_time < 5.0:
            self.send_velocity_commands()
            time.sleep(0.1)


        #make the robot turn itself to 0
        vel_cmd = Twist()
        vel_cmd.angular.z = self.ANG_VEL
        self.vel_pub.publish(vel_cmd)
        #while not within 4° of zero
        while not (-0.0174533*2 < self.current_yaw < 0.0174533*2):
            time.sleep(0.1) # 100ms
        self.vel_pub.publish(Twist())
        
        while (time.time() - start_time) < exploration_time:
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Exploration goal canceled')
                self.stop_robot()
                return result
            
            if self.scan_received:
                self.send_velocity_commands()
            feedback_msg.time_elapsed = time.time() - start_time
            feedback_msg.current_zones = len(
                list(filter(lambda k : self.zones_visited[k], self.zones_visited.keys())))
            feedback_msg.current_state = "turning" if self.turn else "moving forward"
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.1)
        
        self.stop_robot()
        result.total_time = exploration_time
        result.zones_visited = len(list(filter(lambda k : self.zones_visited[k], self.zones_visited.keys())))
        goal_handle.succeed()
        self.get_logger().info(f'Exploration completed! Visited {len(list(filter(lambda k : self.zones_visited[k], self.zones_visited.keys())))} zones')
        return result
    
    def send_velocity_commands(self):
        vel_cmd = Twist()
        fwd_vel = 0.4
        
        if self.turn:
            vel_cmd.linear.x, vel_cmd.angular.z = 0.0, self.ANG_VEL if self.clockwise > 0 else -self.ANG_VEL
        elif self.move_forward:
            vel_cmd.linear.x, vel_cmd.angular.z = fwd_vel, 0.0
        
        self.vel_pub.publish(vel_cmd)
    
    def stop_robot(self):
        self.vel_pub.publish(Twist())

## static methods ##

# x,y of point, x,y of centre of square, side length of square
def is_in_square(x, y, ox, oy, sl):
    return ((ox + (sl/2) < x < ox - (sl/2)) or (ox - (sl/2) < x < ox + (sl/2))) and ((oy + (sl/2) < y < oy - (sl/2)) or (oy - (sl/2) < y < oy + (sl/2)))

def is_in_circle(x, y, ox, oy, r):
    return pow((x - ox), 2) + pow(y - oy, 2) < pow(r, 2)

def clamp_turn_angle(angle):
    if angle < 0:
        angle = min(angle, math.radians(-20))
    else:
        angle = max(angle, math.radians(20))
    return angle

def get_euler_from_quaternion(quat):
    """ Convert quaternion to Euler angles """
    x, y, z, w = quat.x, quat.y, quat.z, quat.w
    sinr_cosp = 2 * (w * x + y * z)
    cosr_cosp = 1 - 2 * (x * x + y * y)
    roll = math.atan2(sinr_cosp, cosr_cosp)
    sinp = 2 * (w * y - z * x)
    pitch = math.asin(sinp) if abs(sinp) <= 1 else math.copysign(math.pi / 2, sinp)
    siny_cosp = 2 * (w * z + x * y)
    cosy_cosp = 1 - 2 * (y * y + z * z)
    yaw = math.atan2(siny_cosp, cosy_cosp)
    return roll, pitch, yaw

    

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