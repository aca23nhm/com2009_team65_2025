#!/usr/bin/env python3

from math import atan2, pi, sqrt
import time
import os
import rclpy
import numpy as np

from ament_index_python.packages import get_package_share_directory
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from rclpy.duration import Duration
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
from sensor_msgs.msg import LaserScan
from nav2_msgs.srv import SaveMap
from cartographer_ros_msgs.srv import FinishTrajectory


class Exploration(Node):

    def __init__(self):
        super().__init__("exploration")

        # Publisher for velocity commands
        self.vel_pub = self.create_publisher(
            msg_type=Twist,
            topic="cmd_vel",
            qos_profile=10,
        )

        # Subscriber for LiDAR data
        self.scan_sub = self.create_subscription(
            LaserScan,
            'scan',
            self.scan_callback,
            10
        )

        # Create subscriber for odometry data
        self.odom_sub = self.create_subscription(
            Odometry,
            'odom',
            self.odom_callback,
            10
        )

        self.save_map_client = self.create_client(
            SaveMap, 
            '/map_saver/save_map'
        )
        
        self.finish_traj_client = self.create_client(FinishTrajectory, "finish_trajectory")

        self.start_time = self.get_clock().now()
        self.exploration_duration = 180.0
        self.exploration_finished = False

        # Initialise position tracking variables
        self.initial_pose_set = False
        self.x0 = 0.0
        self.y0 = 0.0
        self.current_x = 0.0
        self.current_y = 0.0
        self.turn_directions = []
        self.max_memory = 3

        # Initialise variables to hold LiDAR data
        self.obstacle_distance_front = float('inf')  # Default to "no obstacle"
        self.obstacle_distance_left = float('inf')
        self.obstacle_distance_right = float('inf')
        self.lidar_data_received = False  # Flag to track if we've received LiDAR data

        # Initialise velocity message
        self.vel = Twist()

        # Initialise exploration variables
        self.state = "FORWARD"  # Initial state
        self.turn_direction = 1  # 1 for left, -1 for right
        self.stopped = False

        # Set parameters for exploration
        self.safe_distance = 0.40 # Minimum distance to obstacles (metres)
        self.forward_speed = 0.15  # Linear speed (m/s)
        self.turn_speed = 0.6  # Angular speed (rad/s)

        # Levy flight parameters for improved exploration
        self.min_straight_distance = 0.5  # Min distance to travel straight (metres)
        self.max_straight_distance = 2.0  # Max distance to travel straight (metres)
        self.current_straight_target = self.generate_levy_distance()
        self.distance_traveled_since_turn = 0.0
        self.last_position_x = 0.0
        self.last_position_y = 0.0

        # Arena and zone tracking
        self.arena_size = 4.0  # 4x4 meter arena
        self.zone_size = 1.0  # 1x1 meter zones
        self.num_zones = 4  # 4x4 grid of zones

        # Initialise visited zones
        # 2D array: 0 = unvisited, 1 = visited
        self.visited_zones = np.zeros((self.num_zones, self.num_zones), dtype = int)

        # Mark the the central orange zones as visited
        self.visited_zones[1:3, 1:3] = 1

        # Current zone tracking
        self.current_zone_x = None
        self.current_zone_y = None

        self.corner_avoidance_multiplier = 1.6  # Turn faster in corners

        # Create a timer for the control loop (10Hz)
        self.control_timer = self.create_timer(0.1, self.control_loop_callback)

        self.get_logger().info("Exploration node initialised. Starting autonomous exploration.")

        self.shutdown = False

    def scan_callback(self, msg: LaserScan):
        """
        Process incoming LaserScan messages from the robot's LiDAR sensor.
        """
        # Get the ranges array from the message
        ranges = np.array(msg.ranges)

        # Handle out-of-range values (for real robots vs simulation)
        # In simulation, out-of-range is inf, but on real robots it's 0.0
        ranges[(ranges == 0.0) | (ranges == float('inf'))] = msg.range_max

        # Define sectors around the robot
        front_center_indices = list(range(350, 360)) + list(range(0, 10))  # Narrower front
        front_left_indices = list(range(10, 30))  # 10-30 degrees left of center
        front_right_indices = list(range(330, 350))  # 10-30 degrees right of center
        left_indices = list(range(30, 90))  # Wider left
        right_indices = list(range(270, 330))  # Wider right
        rear_indices = list(range(170, 190))  # Approximately behind the robot

        # Extract sector readings for all sectors
        front_center_ranges = ranges[front_center_indices]
        front_left_ranges = ranges[front_left_indices]
        front_right_ranges = ranges[front_right_indices]
        left_ranges = ranges[left_indices]
        right_ranges = ranges[right_indices]
        rear_ranges = ranges[rear_indices]

        # Filter and get minimum distances for all sectors
        valid_front_center = front_center_ranges[(front_center_ranges != float('inf')) & (front_center_ranges > 0.0)]
        valid_front_left = front_left_ranges[(front_left_ranges != float('inf')) & (front_left_ranges > 0.0)]
        valid_front_right = front_right_ranges[(front_right_ranges != float('inf')) & (front_right_ranges > 0.0)]
        valid_left = left_ranges[(left_ranges != float('inf')) & (left_ranges > 0.0)]
        valid_right = right_ranges[(right_ranges != float('inf')) & (right_ranges > 0.0)]
        valid_rear = rear_ranges[(rear_ranges != float('inf')) & (rear_ranges > 0.0)]

        # Update minimum distances in each sector
        self.obstacle_distance_front_center = float(np.min(valid_front_center)) if len(valid_front_center) > 0 else msg.range_max
        self.obstacle_distance_front_left = float(np.min(valid_front_left)) if len(valid_front_left) > 0 else msg.range_max
        self.obstacle_distance_front_right = float(np.min(valid_front_right)) if len(valid_front_right) > 0 else msg.range_max
        self.obstacle_distance_left = float(np.min(valid_left)) if len(valid_left) > 0 else msg.range_max
        self.obstacle_distance_right = float(np.min(valid_right)) if len(valid_right) > 0 else msg.range_max
        self.obstacle_distance_rear = float(np.min(valid_rear)) if len(valid_rear) > 0 else msg.range_max

        # Update minimum distance in the front sector
        self.obstacle_distance_front = min(
            self.obstacle_distance_front_center,
            self.obstacle_distance_front_left,
            self.obstacle_distance_front_right
        )

        # Update flag to indicate that LiDAR data has been received
        self.lidar_data_received = True

    def odom_callback(self, msg: Odometry):
        """
        Process odometry data to track the robot's position and monitor zones.
        """
        # Extract position from odometry message
        x = msg.pose.pose.position.x
        y = msg.pose.pose.position.y

        # Calculate distance moved since last update
        if self.initial_pose_set:
            dx = x - self.last_position_x
            dy = y - self.last_position_y
            distance_moved = sqrt(dx * dx + dy * dy)
            self.distance_traveled_since_turn += distance_moved

        # Store initial position for reference
        if not self.initial_pose_set:
            self.x0 = x
            self.y0 = y
            self.initial_pose_set = True
            self.last_position_x = x
            self.last_position_y = y
            self.get_logger().info(f"Initial position set: x = {self.x0:.2f}, y = {self.y0:.2f}")
        else:
            self.last_position_x = x
            self.last_position_y = y

        # Update current position
        self.current_x = x
        self.current_y = y

        # Calculate relative position
        dx = x - self.x0
        dy = y - self.y0

        # Determine current zone
        zone_x_idx = int((dx + self.arena_size / 2) / self.zone_size)
        zone_y_idx = int((dy + self.arena_size / 2) / self.zone_size)

        # Ensure zone indices are within bounds
        zone_x_idx = max(0, min(zone_x_idx, self.num_zones - 1))
        zone_y_idx = max(0, min(zone_y_idx, self.num_zones - 1))

        # Convert to 1-based for reporting and user interface
        zone_x = zone_x_idx + 1
        zone_y = zone_y_idx + 1

        # If entered a new zone, mark it as visited
        if self.current_zone_x != zone_x_idx or self.current_zone_y != zone_y_idx:
            # Only mark outer zones as visited
            if not (2 <= zone_x <= 3 and 2 <= zone_y <= 3):  # Adjusted for 1-based reporting
                if self.visited_zones[zone_y_idx, zone_x_idx] == 0:  # Still use 0-based for array
                    self.visited_zones[zone_y_idx, zone_x_idx] = 1

                    # Calculate the total number of outer zones visited
                    outer_zones_visited = np.sum(self.visited_zones) - 4  # Subtract the 4 center zones

                    self.get_logger().info(
                        f"New zone entered: ({zone_x}, {zone_y}). "
                        f"Total outer zones visited: {outer_zones_visited}/12."
                    )

        # Update current zone (store 0-based for internal use)
        self.current_zone_x = zone_x_idx
        self.current_zone_y = zone_y_idx

        # Log position periodically
        self.get_logger().info(f"Position: dx = {dx:.2f}m, dy = {dy:.2f}m | Zone: ({zone_x}, {zone_y})", throttle_duration_sec = 5)

    def generate_levy_distance(self):
        """
        Generate a Levy flight distance for straight-line travel.
        """
        # Apply Levy flight distribution (approximated)
        # More small movements, occasional longer ones
        if np.random.random() < 0.2:  # 20% chance of longer movement
            return np.random.uniform(1.0, self.max_straight_distance)
        else:
            return np.random.uniform(self.min_straight_distance, 1.0)

    def is_in_tight_space(self):
        """
        Detect if robot is in a tight space or corner that requires special handling.
        """
        # Front obstacle is close
        front_close = self.obstacle_distance_front < self.safe_distance * 1.1

        # At least one side is also restricted
        side_close = (
            self.obstacle_distance_front_left < self.safe_distance * 1.1 or
            self.obstacle_distance_front_right < self.safe_distance * 1.1
        )

        # Overall space is restricted
        avg_space_restricted = (
            (self.obstacle_distance_front +
            min(self.obstacle_distance_front_left,
                self.obstacle_distance_front_right)) / 2
        ) < self.safe_distance

        return front_close and side_close and avg_space_restricted

    def handle_tight_space(self):
        """
        Special manoeuvre for tight spaces or corners.
        """
        self.get_logger().info("Tight space detected - performing escape manoeuvre.")

        # Try to back up if there's space behind
        if self.obstacle_distance_rear > 0.3:
            self.vel.linear.x = -0.1  # Gentle reverse
        else:
            self.vel.linear.x = 0.0  # Can't back up

        # Turn with increased speed to escape the tight space
        # Use the direction with more space
        if self.obstacle_distance_left > self.obstacle_distance_right:
            turn_dir = 1  # Left
        else:
            turn_dir = -1  # Right

        self.vel.angular.z = self.turn_speed * self.corner_avoidance_multiplier * turn_dir
        self.vel_pub.publish(self.vel)

        # Reset straight line travel target
        self.distance_traveled_since_turn = 0.0
        self.current_straight_target = self.generate_levy_distance()

        return True

    def get_direction_bias(self):
        """
        Calculate a bias for direction selection based on unexplored zones.
        """
        if self.current_zone_x is None or self.current_zone_y is None:
            return 0  # No bias if we don't know position yet

        # Check which zones are unexplored in each cardinal direction
        unexplored_left = 0
        unexplored_right = 0
        unexplored_front = 0
        unexplored_back = 0

        # Check to the left (negative x direction in the grid)
        for i in range(self.current_zone_x):
            for j in range(self.num_zones):
                if self.visited_zones[j, i] == 0 and not (1 <= i <= 2 and 1 <= j <= 2):
                    unexplored_left += 1

        # Check to the right (positive x direction in the grid)
        for i in range(self.current_zone_x + 1, self.num_zones):
            for j in range(self.num_zones):
                if self.visited_zones[j, i] == 0 and not (1 <= i <= 2 and 1 <= j <= 2):
                    unexplored_right += 1

        # Check forward (negative y direction in the grid)
        for j in range(self.current_zone_y):
            for i in range(self.num_zones):
                if self.visited_zones[j, i] == 0 and not (1 <= i <= 2 and 1 <= j <= 2):
                    unexplored_front += 1

        # Check backward (positive y direction in the grid)
        for j in range(self.current_zone_y + 1, self.num_zones):
            for i in range(self.num_zones):
                if self.visited_zones[j, i] == 0 and not (1 <= i <= 2 and 1 <= j <= 2):
                    unexplored_back += 1

        # Log the unexplored counts
        self.get_logger().info(
            f"Unexplored zones - Left: {unexplored_left}, Right: {unexplored_right}, "
            f"Front: {unexplored_front}, Back: {unexplored_back}",
            throttle_duration_sec=5
        )

        # Return a bias: positive for left, negative for right
        # If there's a significant difference, bias toward that direction
        if unexplored_left > unexplored_right + 1:
            return 0.7  # Bias toward left
        elif unexplored_right > unexplored_left + 1:
            return -0.7  # Bias toward right
        else:
            return 0  # No bias

    def select_turn_direction(self):
        """
        Intelligent turn direction selection based on multiple factors.
        """
        direction_scores = {
            "left": 0.0,
            "right": 0.0
        }

        # 1. Obstacle distances (prefer the direction with more space)
        left_space = self.obstacle_distance_left
        right_space = self.obstacle_distance_right

        direction_scores["left"] += left_space * 1.0
        direction_scores["right"] += right_space * 1.0

        # 2. Direction bias from zones and other sources
        bias = self.get_direction_bias()
        if bias > 0:
            direction_scores["left"] += abs(bias) * 0.5
        else:
            direction_scores["right"] += abs(bias) * 0.5

        # 3. Avoid repetitive patterns
        if len(self.turn_directions) >= 3:
            if self.turn_directions[-3:] == [1,1,1]:
                direction_scores["right"] += 1.0  # Bias away from left
            elif self.turn_directions[-3:] == [-1,-1,-1]:
                direction_scores["left"] += 1.0  # Bias away from right

        # 4. Levy flight randomness
        # Occasionally surprising choice
        if np.random.random() < 0.15:  # 15% chance
            if np.random.random() < 0.5:
                direction_scores["left"] += 1.0
            else:
                direction_scores["right"] += 1.0

        # Choose direction with highest score
        if direction_scores["left"] > direction_scores["right"]:
            direction = 1  # Turn left
        else:
            direction = -1  # Turn right

        # Log the decision factors
        self.get_logger().info(
            f"Turn decision - Left score: {direction_scores['left']:.2f}, "
            f"Right score: {direction_scores['right']:.2f}, "
            f"Direction: {'LEFT' if direction == 1 else 'RIGHT'}"
        )

        return direction

    def control_loop_callback(self):
        """
        Main control loop that handles the robot's behaviour.
        """
        # 1) Check if time is up
        if not self.exploration_finished:
            now = self.get_clock().now()
            elapsed_s = (now - self.start_time).nanoseconds * 1e-9
            if elapsed_s >= self.exploration_duration:
                self.exploration_finished = True
                self.get_logger().info("180s have elapsed. Stopping exploration and saving map.")
                self.on_shutdown()
                return

        # 2) If we've already shut down or done exploring, do nothing
        if self.shutdown or not self.lidar_data_received:
            return

        # Check for tight spaces or multiple obstacles
        if self.is_in_tight_space():
            if self.handle_tight_space():
                return

        # Implement the exploration strategy with obstacle avoidance
        if self.state == "FORWARD":
            # If path is clear, move forward
            if self.obstacle_distance_front > self.safe_distance:
                # Check if we've moved far enough in this direction (Levy flight)
                if self.distance_traveled_since_turn > self.current_straight_target:
                    # We've traveled enough in this direction, change to turning state
                    self.state = "TURNING"

                    # Use intelligent turn direction selection
                    self.turn_direction = self.select_turn_direction()

                    # Add to turn directions history
                    if len(self.turn_directions) > self.max_memory:
                        self.turn_directions.pop(0)

                    # Add turn direction to array
                    self.turn_directions.append(self.turn_direction)

                    # Generate new distance target
                    traveled_distance = self.distance_traveled_since_turn  # Store the value before resetting
                    self.current_straight_target = self.generate_levy_distance()
                    self.distance_traveled_since_turn = 0.0

                    self.get_logger().info(
                        f"Levy flight: Changing direction after traveling {traveled_distance:.2f}m. "
                        f"New target: {self.current_straight_target:.2f}m"
                    )
                else:
                    # Continue moving forward
                    self.vel.linear.x = self.forward_speed
                    self.vel.angular.z = 0.0
            else:
                # If obstacle detected, change to turning state
                self.state = "TURNING"

                # Use intelligent turn direction selection
                self.turn_direction = self.select_turn_direction()

                # Add to turn directions history
                if len(self.turn_directions) > self.max_memory:
                    self.turn_directions.pop(0)

                # Add turn direction to array
                self.turn_directions.append(self.turn_direction)

                # Reset distance tracking
                self.distance_traveled_since_turn = 0.0

                self.get_logger().info(
                    f"Obstacle detected at {self.obstacle_distance_front:.2f}m. "
                    f"Turning {'left' if self.turn_direction > 0 else 'right'}."
                )

        elif self.state == "TURNING":
            # Execute turn
            self.vel.linear.x = 0.0  #  forward motion during turn
            self.vel.angular.z = self.turn_speed * self.turn_direction

            # If front is clear after turning enough, resume forward motion
            if self.obstacle_distance_front > self.safe_distance * 1.5:
                self.state = "FORWARD"
                self.get_logger().info("Path clear. Resuming forward motion.")
                # Reset distance tracking after completing a turn
                self.distance_traveled_since_turn = 0.0

        # Publish velocity command
        self.vel_pub.publish(self.vel)

    def on_shutdown(self):
        # Stop the robot
        for _ in range(5):
            self.vel_pub.publish(Twist())

        # Log final exploration result
        outer_zones_visited = np.sum(self.visited_zones) - 4
        self.get_logger().info(f"Final exploration: {outer_zones_visited}/12 outer zones visited.")

        # Unsubscribe from /scan
        self.destroy_subscription(self.scan_sub)
        self.get_logger().info("Unsubscribed from /scan to help finalize Cartographer.")

        # 1) Attempt finish_trajectory
        if self.finish_traj_client.wait_for_service(timeout_sec=5.0):
            req = FinishTrajectory.Request()
            req.trajectory_id = 0
            future = self.finish_traj_client.call_async(req)

            # Give more time (30s) for final optimization
            self.get_logger().info("Calling finish_trajectory, waiting up to 30s.")
            rclpy.spin_until_future_complete(self, future, timeout_sec=30.0)
            if future.result() is not None:
                self.get_logger().info("FinishTrajectory call succeeded. Cartographer should finalize now.")
                time.sleep(3)
            else:
                self.get_logger().warn("FinishTrajectory call timed out or failed.")
        else:
            self.get_logger().warn("'finish_trajectory' service not available.")

        # 2) Save the map
        self.get_logger().info("Attempting to save map via service call...")
        if self.save_map_client.wait_for_service(timeout_sec=5.0):
            request = SaveMap.Request()
            maps_dir = "/home/student/ros2_ws/src/com2009_team65_2025/maps"
            os.makedirs(maps_dir, exist_ok=True)
            map_prefix = os.path.join(maps_dir, 'arena_map')

            request.map_url = map_prefix
            request.image_format = 'png'
            request.free_thresh = 0.25
            request.occupied_thresh = 0.65

            future = self.save_map_client.call_async(request)
            rclpy.spin_until_future_complete(self, future, timeout_sec=30.0)
            if future.result() is not None:
                self.get_logger().info("Map saved successfully!")
            else:
                self.get_logger().warn("Failed to save the map. Possibly timed out.")
        else:
            self.get_logger().warn("/map_saver/save_map service not available.")

        self.shutdown = True

def main(args=None):
    rclpy.init(
        args=args,
        signal_handler_options=SignalHandlerOptions.NO
    )
    node = Exploration()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.on_shutdown()
    finally:
        while not node.shutdown:
            continue
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
