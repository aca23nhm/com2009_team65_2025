#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import numpy as np
import time
import os
from math import sqrt, atan2, cos, sin, pi
from random import random, uniform
from functools import partial

# Import ROS2 message and service types
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool
from cartographer_ros_msgs.srv import FinishTrajectory
from rclpy.duration import Duration


class MapExplorerRobot(Node):
    """
    An autonomous robot controller that explores an environment and builds a map.
    Uses a combination of strategies including obstacle avoidance and randomized
    motion patterns to maximize coverage of the environment.
    """
    
    def __init__(self):
        """Initialize the explorer robot with necessary publishers, subscribers and parameters."""
        super().__init__('autonomous_explorer')
        
        # Set up robot motion control
        self.motion_publisher = self.create_publisher(Twist, 'cmd_vel', 10)
        
        # Set up sensor and telemetry subscribers
        self.range_subscriber = self.create_subscription(
            LaserScan, 'scan', self._process_lidar_data, 10)
        self.position_subscriber = self.create_subscription(
            Odometry, 'odom', self._update_position_data, 10)
        
        # Set up mapping system interaction
        self.exploration_complete_publisher = self.create_publisher(Bool, '/exploration_done', 10)
        self.trajectory_service = self.create_client(FinishTrajectory, "finish_trajectory")
        
        # Setup robot motion parameters
        self.linear_velocity = 0.20  # Forward speed in m/s
        self.rotation_velocity = 0.6  # Rotation speed in rad/s
        self.safe_distance = 0.40  # Minimum safe distance to obstacles
        
        # Initialize state variables
        self.robot_state = "EXPLORE_FORWARD"
        self.robot_command = Twist()
        self.lidar_initialized = False
        self.system_shutdown = False
        
        # Position tracking
        self.position_initialized = False
        self.origin_x = 0.0
        self.origin_y = 0.0
        self.current_position = {"x": 0.0, "y": 0.0}
        self.previous_position = {"x": 0.0, "y": 0.0}
        
        # Movement strategy
        self.turn_preference = 1  # Initial turn preference (1=clockwise, -1=counter-clockwise)
        self.turn_history = []
        self.memory_length = 3
        self.distance_since_last_turn = 0.0
        self.target_segment_length = self._generate_segment_length()
        
        # Environment mapping
        self.environment_width = 4.0
        self.sector_width = 1.0
        self.grid_dimension = 3
        self.visited_grid = np.zeros((self.grid_dimension, self.grid_dimension), dtype=int)
        
        # Mark center sectors as already visited (orange zone)
        self.visited_grid[1:3, 1:3] = 1
        
        # Current sector position
        self.current_sector = {"x": None, "y": None}
        
        # Sensor data storage
        self.sensor_readings = {
            "front": float('inf'),
            "front_left": float('inf'),
            "front_right": float('inf'),
            "left": float('inf'),
            "right": float('inf'),
            "rear": float('inf')
        }
        
        # Exploration timer
        self.start_time = self.get_clock().now()
        self.max_exploration_time = 180.0  # 3 minutes
        self.exploration_ended = False
        
        # Start control loop at 10Hz
        self.control_loop = self.create_timer(0.1, self._navigation_control_loop)
        
        self.get_logger().info("Map Explorer initialized - beginning autonomous navigation")
    
    def _process_lidar_data(self, scan_data: LaserScan):
        """Process incoming laser scan data to detect obstacles in different directions."""
        # Convert scan data to numpy array for efficient processing
        ranges = np.array(scan_data.ranges)
        
        # Replace invalid readings with max range
        invalid_mask = (ranges == 0.0) | (ranges == float('inf'))
        ranges[invalid_mask] = scan_data.range_max
        
        # Define angle sectors (in degrees)
        sectors = {
            "front": list(range(350, 360)) + list(range(0, 10)),
            "front_left": list(range(10, 30)),
            "front_right": list(range(330, 350)),
            "left": list(range(30, 90)),
            "right": list(range(270, 330)),
            "rear": list(range(170, 210))
        }
        
        # Process each sector
        for sector_name, indices in sectors.items():
            sector_ranges = ranges[indices]
            valid_readings = sector_ranges[(sector_ranges != float('inf')) & (sector_ranges > 0.0)]
            
            if len(valid_readings) > 0:
                self.sensor_readings[sector_name] = float(np.min(valid_readings))
            else:
                self.sensor_readings[sector_name] = scan_data.range_max
        
        # Calculate combined front distance
        self.sensor_readings["front"] = min(
            self.sensor_readings["front"],
            self.sensor_readings["front_left"],
            self.sensor_readings["front_right"]
        )
        
        # Set flag that we've received lidar data
        self.lidar_initialized = True
    
    def _update_position_data(self, odom_data: Odometry):
        """Track robot position and update coverage map."""
        # Extract position data
        pos_x = odom_data.pose.pose.position.x
        pos_y = odom_data.pose.pose.position.y
        
        # Store initial position as origin
        if not self.position_initialized:
            self.origin_x = pos_x
            self.origin_y = pos_y
            self.position_initialized = True
            self.previous_position["x"] = pos_x
            self.previous_position["y"] = pos_y
            self.get_logger().info(f"Origin set: ({self.origin_x:.2f}, {self.origin_y:.2f})")
        else:
            # Calculate distance moved since last update
            dx = pos_x - self.previous_position["x"]
            dy = pos_y - self.previous_position["y"]
            movement = sqrt(dx*dx + dy*dy)
            self.distance_since_last_turn += movement
            
            # Update position history
            self.previous_position["x"] = pos_x
            self.previous_position["y"] = pos_y
        
        # Update current position
        self.current_position["x"] = pos_x
        self.current_position["y"] = pos_y
        
        # Calculate position relative to origin
        rel_x = pos_x - self.origin_x
        rel_y = pos_y - self.origin_y
        
        # Determine current sector (grid cell)
        sector_x = int((rel_x + self.environment_width / 2) / self.sector_width)
        sector_y = int((rel_y + self.environment_width / 2) / self.sector_width)
        
        # Ensure sector indices are within bounds
        sector_x = max(0, min(sector_x, self.grid_dimension - 1))
        sector_y = max(0, min(sector_y, self.grid_dimension - 1))
        
        # Convert to 1-based coordinates for logging
        display_x = sector_x + 1
        display_y = sector_y + 1
        
        # If we entered a new sector, mark it as visited
        if self.current_sector["x"] != sector_x or self.current_sector["y"] != sector_y:
            # Only mark non-orange sectors as visited
            if not (1 <= sector_x <= 2 and 1 <= sector_y <= 2):
                if self.visited_grid[sector_y, sector_x] == 0:
                    self.visited_grid[sector_y, sector_x] = 1
                    
                    # Calculate total visited sectors
                    total_visited = np.sum(self.visited_grid)
                    
                    self.get_logger().info(
                        f"Entered new sector: ({display_x}, {display_y}). "
                        f"Total visited: {total_visited}/12."
                    )
        
        # Update current sector
        self.current_sector["x"] = sector_x
        self.current_sector["y"] = sector_y
        
        # Log position periodically (every 5 seconds)
        self.get_logger().info(
            f"Position: ({rel_x:.2f}, {rel_y:.2f}) | Sector: ({display_x}, {display_y})",
            throttle_duration_sec=5
        )
    
    def _navigation_control_loop(self):
        """Main control loop that manages robot navigation behavior."""
        # Check if exploration time limit has been reached
        if not self.exploration_ended:
            current_time = self.get_clock().now()
            elapsed_time = (current_time - self.start_time).nanoseconds * 1e-9
            
            if elapsed_time >= self.max_exploration_time:
                self.exploration_ended = True
                self.get_logger().info("Exploration time limit reached. Finalizing map...")
                self._finalize_exploration()
                return
        
        # Skip processing if we're shutting down or haven't received sensor data yet
        if self.system_shutdown or not self.lidar_initialized:
            return
        
        # Check if we're in a constrained space that needs special handling
        if self._is_confined_space():
            if self._handle_confined_space():
                return
        
        # Main navigation state machine
        if self.robot_state == "EXPLORE_FORWARD":
            # Check if path is clear ahead
            if self.sensor_readings["front"] > self.safe_distance:
                # Check if we've moved far enough in this direction
                if self.distance_since_last_turn > self.target_segment_length:
                    # Switch to turning state
                    self.robot_state = "CHANGE_DIRECTION"
                    
                    # Choose turn direction intelligently
                    self.turn_preference = self._select_optimal_direction()
                    
                    # Update turn history
                    if len(self.turn_history) >= self.memory_length:
                        self.turn_history.pop(0)
                    self.turn_history.append(self.turn_preference)
                    
                    # Record distance traveled and generate new target
                    distance_traveled = self.distance_since_last_turn
                    self.target_segment_length = self._generate_segment_length()
                    self.distance_since_last_turn = 0.0
                    
                    self.get_logger().info(
                        f"Changing direction after {distance_traveled:.2f}m. "
                        f"New target distance: {self.target_segment_length:.2f}m"
                    )
                else:
                    # Continue moving forward
                    self.robot_command.linear.x = self.linear_velocity
                    self.robot_command.angular.z = 0.0
            else:
                # Obstacle ahead, need to turn
                self.robot_state = "CHANGE_DIRECTION"
                
                # Choose turn direction intelligently
                self.turn_preference = self._select_optimal_direction()
                
                # Update turn history
                if len(self.turn_history) >= self.memory_length:
                    self.turn_history.pop(0)
                self.turn_history.append(self.turn_preference)
                
                # Reset distance counter
                self.distance_since_last_turn = 0.0
                
                self.get_logger().info(
                    f"Obstacle at {self.sensor_readings['front']:.2f}m. "
                    f"Turning {self._direction_to_string(self.turn_preference)}."
                )
        
        elif self.robot_state == "CHANGE_DIRECTION":
            # Execute turn maneuver
            self.robot_command.linear.x = 0.0
            self.robot_command.angular.z = self.rotation_velocity * self.turn_preference
            
            # Check if we've turned enough to resume forward motion
            if self.sensor_readings["front"] > self.safe_distance * 1.5:
                self.robot_state = "EXPLORE_FORWARD"
                self.get_logger().info("Path now clear. Moving forward.")
                self.distance_since_last_turn = 0.0
        
        # Send movement command to robot
        self.motion_publisher.publish(self.robot_command)
    
    def _is_confined_space(self):
        """Detect if robot is in a confined space or corner."""
        # Check if front is obstructed
        front_blocked = self.sensor_readings["front"] < self.safe_distance
        
        # Check if sides are also restricted
        sides_restricted = (
            self.sensor_readings["front_left"] < self.safe_distance or
            self.sensor_readings["front_right"] < self.safe_distance
        )
        
        # Check average space around robot
        avg_space = (
            self.sensor_readings["front"] +
            min(self.sensor_readings["front_left"], self.sensor_readings["front_right"])
        ) / 2 < self.safe_distance
        
        return front_blocked and sides_restricted and avg_space
    def _handle_confined_space(self):
        """Execute special operation to escape confined spaces."""
        self.get_logger().info("Confined space detected - executing escape operation")
        
        # Try to back up if there's space
        if self.sensor_readings["rear"] > 0.3:
            self.robot_command.linear.x = -0.05  # Gentle reverse
        else:
            self.robot_command.linear.x = 0.0  # Can't back up
        
        # Turn toward direction with more space
        if self.sensor_readings["left"] > self.sensor_readings["right"]:
            escape_direction = 1  # Turn left
        else:
            escape_direction = -1  # Turn right
        
        # Apply increased rotation for quicker escape
        self.robot_command.angular.z = self.rotation_velocity * 1.6 * escape_direction
        self.motion_publisher.publish(self.robot_command)
        
        # Reset distance tracking
        self.distance_since_last_turn = 0.0
        self.target_segment_length = self._generate_segment_length()
        
        return True
    
    def _generate_segment_length(self):
        """Generate a variable segment length using modified Levy flight pattern."""
        # Apply Levy-like distribution (more short moves, occasional long ones)
        if random() < 0.6:  # 20% chance of longer movement
            return uniform(1.0, 3.0)
        else:
            return uniform(0.5, 1.0)
    
    def _calculate_exploration_bias(self):
        """Calculate directional bias based on unexplored sectors."""
        if self.current_sector["x"] is None or self.current_sector["y"] is None:
            return 0  # No bias if position unknown
        
        # Count unexplored sectors in each direction
        unexplored = {
            "left": 0,
            "right": 0,
            "front": 0,
            "back": 0
        }
        
        # Check left direction (-x in grid)
        for x in range(self.current_sector["x"]):
            for y in range(self.grid_dimension):
                if self.visited_grid[y, x] == 0 and not (1 <= x <= 2 and 1 <= y <= 2):
                    unexplored["left"] += 1
        
        # Check right direction (+x in grid)
        for x in range(self.current_sector["x"] + 1, self.grid_dimension):
            for y in range(self.grid_dimension):
                if self.visited_grid[y, x] == 0 and not (1 <= x <= 2 and 1 <= y <= 2):
                    unexplored["right"] += 1
        
        # Check front direction (-y in grid)
        for y in range(self.current_sector["y"]):
            for x in range(self.grid_dimension):
                if self.visited_grid[y, x] == 0 and not (1 <= x <= 2 and 1 <= y <= 2):
                    unexplored["front"] += 1
        
        # Check back direction (+y in grid)
        for y in range(self.current_sector["y"] + 1, self.grid_dimension):
            for x in range(self.grid_dimension):
                if self.visited_grid[y, x] == 0 and not (1 <= x <= 2 and 1 <= y <= 2):
                    unexplored["back"] += 1
        
        # Log unexplored counts periodically
        self.get_logger().info(
            f"Unexplored - L: {unexplored['left']}, R: {unexplored['right']}, "
            f"F: {unexplored['front']}, B: {unexplored['back']}",
            throttle_duration_sec=5
        )
        
        # Calculate bias (positive for left turn, negative for right turn)
        if unexplored["left"] > unexplored["right"] + 1:
            return 0.7  # Left bias
        elif unexplored["right"] > unexplored["left"] + 1:
            return -0.7  # Right bias
        else:
            return 0  # No strong bias
    
    def _select_optimal_direction(self):
        """Choose optimal turn direction based on multiple factors."""
        scores = {"left": 0.0, "right": 0.0}
        
        # Factor 1: Available space in each direction
        scores["left"] += self.sensor_readings["left"] * 1.0
        scores["right"] += self.sensor_readings["right"] * 1.0
        
        # Factor 2: Exploration bias from unexplored sectors
        bias = self._calculate_exploration_bias()
        if bias > 0:
            scores["left"] += abs(bias) * 0.5
        else:
            scores["right"] += abs(bias) * 0.5
        
        # Factor 3: Avoid repetitive turning patterns
        if len(self.turn_history) >= 3:
            if self.turn_history[-3:] == [1, 1, 1]:
                scores["right"] += 1.0  # Avoid turning left again
            elif self.turn_history[-3:] == [-1, -1, -1]:
                scores["left"] += 1.0  # Avoid turning right again
        
        # Factor 4: Random variation (Levy-inspired)
        if random() < 0.15:  # 15% chance of surprising choice
            if random() < 0.5:
                scores["left"] += 1.0
            else:
                scores["right"] += 1.0
        
        # Choose direction with highest score
        direction = 1 if scores["left"] > scores["right"] else -1
        
        # Log decision factors
        self.get_logger().info(
            f"Turn decision - Left: {scores['left']:.2f}, Right: {scores['right']:.2f}, "
            f"Selected: {self._direction_to_string(direction)}"
        )
        
        return direction
    
    def _direction_to_string(self, direction):
        """Convert direction value to string representation."""
        return "LEFT" if direction > 0 else "RIGHT"
    
    def _finalize_exploration(self):
        """Finalize exploration and save the generated map."""
        # Stop the robot
        for _ in range(5):
            self.motion_publisher.publish(Twist())
        
        # Log exploration summary
        total_visited = np.sum(self.visited_grid)
        self.get_logger().info(f"Exploration complete: {total_visited}/9 sectors visited.")
        
        # Notify that exploration is complete (triggers map saving)
        complete_msg = Bool(data=True)
        self.exploration_complete_publisher.publish(complete_msg)
        self.get_logger().info("Published exploration_done message")
        
        # Unsubscribe from scan to help Cartographer finalize
        self.destroy_subscription(self.range_subscriber)
        self.get_logger().info("Unsubscribed from scan topic to assist map finalization")
        
        # Call Cartographer's finish_trajectory service
        if self.trajectory_service.wait_for_service(timeout_sec=5.0):
            request = FinishTrajectory.Request()
            request.trajectory_id = 0
            future = self.trajectory_service.call_async(request)
            
            # Wait for service to complete
            self.get_logger().info("Calling finish_trajectory service, waiting up to 30s")
            rclpy.spin_until_future_complete(self, future, timeout_sec=30.0)
            
            if future.result() is not None:
                self.get_logger().info("FinishTrajectory call succeeded. Map should be finalized.")
                time.sleep(3)
            else:
                self.get_logger().warn("FinishTrajectory call failed or timed out.")
        else:
            self.get_logger().warn("finish_trajectory service not available")
        
        self.system_shutdown = True


def main(args=None):
    """Main function to initialize and run the explorer node."""
    rclpy.init(
        args=args,
        signal_handler_options=SignalHandlerOptions.NO
    )
    
    explorer = MapExplorerRobot()
    
    try:
        rclpy.spin(explorer)
    except KeyboardInterrupt:
        explorer._finalize_exploration()
    finally:
        # Wait for shutdown to complete
        while not explorer.system_shutdown:
            continue
        explorer.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()