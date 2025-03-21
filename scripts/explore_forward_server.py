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

        self.MIN_DISTANCE = 0.5 # Keep the same distance threshold as original
        self.MINIMUM_SAFE_TURN = math.radians(20)
        self.ANG_VEL = 0.8

        self.turn_duration = 0.0
        self.turn_start_time = 0.0
        self.clockwise = True
        self.zones_visited = set()
        self.current_x = 0.0
        self.current_y = 0.0
        self.current_yaw = 0.0
        
        self.ARENA_SIZE = 4.0
        self.ZONE_SIZE = 1.0
        
        # coordinates, from origin, in metres, of the centres of all of the zones
        # top row + bottom row + sides   1 2 3 4                      5              6                   7  8  9  10                                11          12   
        zones : list = [(-1.5, y/10) for y in range(-15, 20, 10)] + [(-0.5, 1.5), (0.5, 1.5)] + [(1.5, y/10) for y in range(15, -20, -10) ] + [(0.5, -1.5), (-0.5, -1.5)]
        self.zones_visited = dict(zip(zones, [False] * len(zones))) # dict with zones as keys and bools as values
        
        # Keep a separate list of target zones to prioritize (can be dynamically updated)
        self.target_zones = list(self.zones_visited.keys())
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
            
            # Remove this zone from target zones list to avoid revisiting
            if current_square in self.target_zones:
                self.target_zones.remove(current_square)
                self.get_logger().info(f"Removed Zone {self.zone_at_coords((current_square[0], current_square[1]))} from target zones")
                self.get_logger().info(f"Remaining target zones: {[self.zone_at_coords(z) for z in self.target_zones]}")

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
        point_to_angle = lambda k: abs(math.acos(self.cos_angle_to_point(*k)))

        # Get only unvisited target zones
        unvisited = [k for k in self.target_zones if not self.zones_visited[k]]

        if not unvisited:
            self.get_logger().info("All zones visited, stopping exploration.")
            self.stop_robot()
            return 0.0  # Stop turning

        # Sort unvisited zones by angle
        unvisited.sort(key=point_to_angle)

        # Pick the closest unvisited zone
        target = unvisited[0]

        self.get_logger().info(f"Turning towards new unvisited Zone {self.zone_at_coords(target)}")
        angle = math.acos(self.cos_angle_to_point(target[0], target[1]))

        self.turn_clockwise = angle > 0
        return angle

    def update_movement_state(self):
        # This keeps the original obstacle detection logic 
        if self.is_front_obstacle() and not self.turn:
            self.move_forward = False
            self.turn = True
            
            # Calculate turn angle based on target zones
            self.turn_start_time = time.time()
            turn_angle = clamp_turn_angle(self.find_direction_to_turn_to_zone_based())
            time_to_turn = abs(turn_angle / self.ANG_VEL)
            self.turn_duration = time_to_turn

            self.get_logger().info(f"Turning {math.degrees(turn_angle):.1f}° - turning for {time_to_turn:.2f} seconds {'anti' if not self.turn_clockwise else ''}clockwise")
        elif self.turn and (time.time() - self.turn_start_time > self.turn_duration):
            self.turn = False
            self.move_forward = True
    
    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing exploration...')
        exploration_time = goal_handle.request.exploration_time
        feedback_msg = ExploreForward.Feedback()
        result = ExploreForward.Result()

        start_time = time.time()

        # Reinitialize zones_visited and target_zones
        zones: list = [(-1.5, y/10) for y in range(-15, 20, 10)] + [(-0.5, 1.5), (0.5, 1.5)] + [(1.5, y/10) for y in range(15, -20, -10)] + [(0.5, -1.5), (-0.5, -1.5)]
        self.zones_visited = dict(zip(zones, [False] * len(zones)))

        # Initialize target zones to focus on outer zones first
        outer_zones = [zone for zone in zones if abs(zone[0]) == 1.5 or abs(zone[1]) == 1.5]
        self.target_zones = outer_zones + [z for z in zones if z not in outer_zones]
        self.get_logger().info(f"Target zones initialized with {len(self.target_zones)} zones, prioritizing outer zones")

        # Wait for scan data for up to 5 seconds before moving
        while not self.scan_received and time.time() - start_time < 5.0:
            self.send_velocity_commands()
            time.sleep(0.1)

        # Main exploration loop (up to 90 seconds or user-defined time)
        while (time.time() - start_time) < min(exploration_time, 90):
            if goal_handle.is_cancel_requested:
                goal_handle.canceled()
                self.get_logger().info('Exploration goal canceled')
                self.stop_robot()
                return result

            if self.scan_received:
                self.send_velocity_commands()

            # Update feedback
            feedback_msg.time_elapsed = time.time() - start_time
            feedback_msg.current_zones = sum(self.zones_visited.values())
            feedback_msg.current_state = "turning towards zone" if self.turn else "moving forward"

            # Calculate percentage of target zones visited
            if self.target_zones:
                completion = (1 - len(self.target_zones) / len(self.zones_visited)) * 100
                self.get_logger().info(f"Exploration progress: {completion:.1f}% (Remaining: {len(self.target_zones)})")
            else:
                self.get_logger().info("All target zones visited!")

            goal_handle.publish_feedback(feedback_msg)
            time.sleep(0.1)

        # Stop the robot and return results
        self.stop_robot()
        result.total_time = float(min(exploration_time, 90))
        result.zones_visited = sum(self.zones_visited.values())
        goal_handle.succeed()
        self.get_logger().info(f'Exploration completed! Visited {result.zones_visited} zones')
        return result
    
    def send_velocity_commands(self):
        vel_cmd = Twist()
        fwd_vel = 0.26
        
        if self.turn:
            vel_cmd.linear.x = -0.05
            vel_cmd.angular.z = self.ANG_VEL if self.turn_clockwise else - self.ANG_VEL
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
    try:
        # Initialize ROS 2
        rclpy.init(args=args)

        # Create and initialize the server node
        exploration_server = ExploreForwardServer()

        # Create the executor to handle the server node
        executor = MultiThreadedExecutor()
        executor.add_node(exploration_server)

        # Spin the executor, which will keep the server alive
        executor.spin()

    except KeyboardInterrupt:
        print("Keyboard interrupt received, shutting down...")

    finally:
        # Ensure the node is destroyed and shutdown is only called once
        if rclpy.ok():
            exploration_server.destroy_node()
            rclpy.shutdown()

if __name__ == "__main__":
    main()