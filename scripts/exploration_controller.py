#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions
import numpy as np
import time
import os
import cv2
from math import sqrt, atan2, cos, sin, pi, degrees, radians
from random import random, uniform
from functools import partial

# Import ROS2 message and service types
from geometry_msgs.msg import Twist
from sensor_msgs.msg import LaserScan
from nav_msgs.msg import Odometry
from std_msgs.msg import Bool
from cartographer_ros_msgs.srv import FinishTrajectory
from rclpy.duration import Duration
from com2009_team65_2025.srv import ControlSharingReq


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
        self.safe_distance = 0.42  # Minimum safe distance to obstacles
        
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
        self.grid_dimension = 3
        self.sector_width = self.environment_width / self.grid_dimension
        self.visited_grid = np.zeros((self.grid_dimension, self.grid_dimension), dtype=int)

        # Room exploration parameters
        self.room_entrance_threshold = 0.6  # Width threshold for room entrance (meters)
        self.room_detection_window = 20  # Degrees each side of center to check for entrance
        self.entrance_detected = False
        self.entrance_approach_count = 0
        self.max_entrance_attempts = 3  # Max attempts to enter a detected entrance
        self.entrance_approach_angle = 0.0
        self.entrance_approach_start_time = None
        self.entrance_approach_timeout = 5.0  # seconds to attempt entrance
        
        # Room entry state machine
        self.room_entry_state = "IDLE"  # IDLE, ALIGNING, ENTERING, COMPLETED
        
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

        # Create a server for the control taker overer
        self.has_control = True
        self.control_relinquisher = self.create_service(
            srv_type=ControlSharingReq,
            srv_name='exploration_controller_control_controller',
            callback = self.control_relinquisher_callback
        )
        
        self.get_logger().info("Map Explorer initialized - beginning autonomous navigation")

    def _detect_room_entrance(self, ranges):
        """
        Detect potential room entrances by looking for openings in walls.
        Returns angle to center of detected entrance or None if none found.
        """
        # Hardcoded: assuming 360° LIDAR with 1° resolution and 0° at index 0
        total_degrees = len(ranges)
        center_index = total_degrees // 2  # Should correspond to front (180°)

        window = self.room_detection_window  # e.g., 20
        start_index = center_index - window
        end_index = center_index + window
        start_index = max(0, start_index)
        end_index = min(len(ranges), end_index)

        front_ranges = ranges[start_index:end_index]

        entrance_threshold = 0.4
        current_entrance = None
        potential_entrances = []

        for i, r in enumerate(front_ranges):
            if r > entrance_threshold:
                if current_entrance is None:
                    current_entrance = [i, i]
                else:
                    current_entrance[1] = i
            else:
                if current_entrance is not None:
                    idx1, idx2 = current_entrance
                    width_angle = idx2 - idx1
                    avg_range = np.mean(front_ranges[idx1:idx2+1])
                    width = 2 * avg_range * sin(radians(width_angle / 2))
                    if width >= self.room_entrance_threshold:
                        center_angle = (idx1 + idx2) / 2
                        angle_relative = center_angle - window
                        potential_entrances.append((angle_relative, width))
                    current_entrance = None

        if current_entrance is not None:
            idx1, idx2 = current_entrance
            width_angle = idx2 - idx1
            avg_range = np.mean(front_ranges[idx1:idx2+1])
            width = 2 * avg_range * sin(radians(width_angle / 2))
            if width >= self.room_entrance_threshold:
                center_angle = (idx1 + idx2) / 2
                angle_relative = center_angle - window
                potential_entrances.append((angle_relative, width))

        if potential_entrances:
            best = max(potential_entrances, key=lambda x: x[1])
            self.get_logger().info(
                f"Detected entrance at {best[0]:.1f}° (width: {best[1]:.2f}m)"
            )
            return best[0]

        return None

    
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

        # Check for room entrances (unless we're already handling one)
        if self.room_entry_state == "IDLE":
            entrance_angle = self._detect_room_entrance(ranges)
            if entrance_angle is not None:
                self.entrance_detected = True
                self.entrance_approach_angle = entrance_angle
                self.entrance_approach_count = 0
                self.room_entry_state = "ALIGNING"
                self.entrance_approach_start_time = self.get_clock().now()
                self.get_logger().info(f"Starting room entry procedure for entrance at {entrance_angle:.1f}°")
        else:
            self.entrance_detected = False
        
        # Set flag that we've received lidar data
        self.lidar_initialized = True

    def _handle_room_entry(self):
        """State machine for handling room entry procedure."""
        current_time = self.get_clock().now()
        elapsed_time = (current_time - self.entrance_approach_start_time).nanoseconds * 1e-9
        
        # Check for timeout
        if elapsed_time > self.entrance_approach_timeout:
            self.get_logger().warn("Room entry timed out. Resuming exploration.")
            self.room_entry_state = "IDLE"
            self.entrance_detected = False
            self.entrance_approach_count += 1
            return False
        
        if self.room_entry_state == "ALIGNING":
            # Align robot with the entrance
            angle_threshold = radians(5)  # 5 degrees in radians
            
            # Calculate remaining angle to align
            remaining_angle = radians(self.entrance_approach_angle)
            
            if abs(remaining_angle) > angle_threshold:
                # Continue aligning
                self.robot_command.linear.x = 0.0
                self.robot_command.angular.z = np.sign(remaining_angle) * min(
                    self.rotation_velocity * 0.7,
                    abs(remaining_angle) * 2.0  # Proportional control
                )
                self.get_logger().info(
                    f"Aligning with room entrance (remaining: {degrees(remaining_angle):.1f}°)",
                    throttle_duration_sec=1.0
                )
            else:
                # Alignment complete, start entering
                self.room_entry_state = "ENTERING"
                self.get_logger().info("Alignment complete. Starting to enter room.")
                self.entrance_approach_start_time = current_time  # Reset timer for entering phase
        
        elif self.room_entry_state == "ENTERING":
            # Move forward into the room while checking for obstacles
            if self.sensor_readings["front"] > self.safe_distance * 1.2:
                # Path is clear, continue forward
                self.robot_command.linear.x = self.linear_velocity * 0.8  # Slightly slower
                self.robot_command.angular.z = 0.0
                
                # Check if we've entered far enough (1 meter or hit timeout)
                if elapsed_time > 2.0:  # After 2 seconds of moving forward
                    self.room_entry_state = "COMPLETED"
                    self.get_logger().info("Room entry completed successfully.")
            else:
                # Obstacle detected during entry
                self.get_logger().warn("Obstacle detected during room entry. Aborting.")
                self.room_entry_state = "IDLE"
                self.entrance_approach_count += 1
                return False
        
        elif self.room_entry_state == "COMPLETED":
            # Entry completed successfully
            self.room_entry_state = "IDLE"
            self.entrance_detected = False
            return True
        
        # Publish the movement command
        self.motion_publisher.publish(self.robot_command)
        return True
    
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
            self.current_position["x"] = pos_x
            self.current_position["y"] = pos_y

            # Use actual position, not relative to origin
            sector_x = int((pos_x + self.environment_width / 2) / self.sector_width)
            sector_y = int((pos_y + self.environment_width / 2) / self.sector_width)
            sector_x = max(0, min(sector_x, self.grid_dimension - 1))
            sector_y = max(0, min(sector_y, self.grid_dimension - 1))

            self.current_sector["x"] = sector_x
            self.current_sector["y"] = sector_y
            self.visited_grid[sector_y, sector_x] = 1

            self.get_logger().info(
                f"Origin set: ({self.origin_x:.2f}, {self.origin_y:.2f}) | "
                f"Initial sector marked visited: ({sector_x + 1}, {sector_y + 1})"
            )
            return

        # Calculate distance moved since last update
        dx = pos_x - self.previous_position["x"]
        dy = pos_y - self.previous_position["y"]
        movement = sqrt(dx * dx + dy * dy)
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
        sector_x = max(0, min(sector_x, self.grid_dimension - 1))
        sector_y = max(0, min(sector_y, self.grid_dimension - 1))

        # Convert to 1-based coordinates for logging
        display_x = sector_x + 1
        display_y = sector_y + 1

        # If we entered a new sector, mark it as visited
        if self.current_sector["x"] != sector_x or self.current_sector["y"] != sector_y:
            if self.visited_grid[sector_y, sector_x] == 0:
                self.visited_grid[sector_y, sector_x] = 1

                total_visited = np.sum(self.visited_grid)
                self.get_logger().info(
                    f"Entered new sector: ({display_x}, {display_y}). "
                    f"Total visited: {total_visited}/9."
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
        
        # Skip processing if we're shutting down, haven't received sensor data yet, or if we don't have control
        if self.system_shutdown or not self.lidar_initialized or not self.has_control:
            return
        
        # Handle room entry procedure if active
        if self.room_entry_state != "IDLE":
            if self._handle_room_entry():
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
        if not self.has_control:
            return False
            
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
        """Execute special maneuver to escape confined spaces."""
        self.get_logger().info("Confined space detected - executing escape maneuver")
        
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
        if random() < 0.6:  # 60% chance of longer movement
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


    def control_relinquisher_callback(self, request, response):
        if request.giving_back:
            self.get_logger().info("The BeaconDetector has given us control back.")
            self.has_control = True
            response.do_you_have_control = False
        else:
            self.get_logger().info("The BeaconDetector has requested control.")
            self.has_control = False
            response.do_you_have_control = True 
            self.motion_publisher.publish(Twist())   
        return response        

    def shutdown_ops(self):
            self.get_logger().info(
                "Shutting down..."
            )
            cv2.destroyAllWindows()
            for i in range(5):
                self.motion_publisher.publish(Twist())
            self.shutdown = True

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
        explorer.shutdown_ops()
        explorer.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()