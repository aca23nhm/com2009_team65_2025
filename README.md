# TurtleBot Autonomous Explorer

## Summary

This ROS2 Python application enables a TurtleBot3 Waffle to autonomously explore an arena within 3 minutes, avoiding obstacles and building an occupancy grid via SLAM. It uses LiDAR and odometry data to detect and navigate around obstacles while marking visited areas on a 3×3 grid. The robot moves in randomized segments with adaptive turning. Using the ROS2 node `BeaconDetector`, it identifies coloured beacons using the robot's built-in camera. A photo is captured and saved locally when the target colour is detected. 

The system combines autonomous navigation, visual detection, and map generation for efficient environment exploration and documentation.

## Installation and Execution

This guide assumes ROS2 has been installed via [the University's Guide](https://tom-howard.github.io/com2009/ros/).

This guide is intended for people running our code on a real-life robot.

### Cloning the Repository

To clone our repository, navigate to `~/ros2_ws/src/` and run:

```bash
git clone https://github.com/aca23nhm/com2009_team65_2025.git
```

This will install all our packages into your workspace ready to be run.

### Packages used

Our package requires the following python/ros2 packages to be installed in order to work properly:
- rclpy
- sensor_msgs
- geometry_msgs
- nav_msgs
- std_msgs
- cartographer_ros_msgs
- cv2
- ament_index_python

### Pairing the Robot

This guide assumes you are already familiar with the robot pairing process.

### Running the Navigation Program

Navigate to `~/ros2_ws/src` in a terminal and run the following commands:

```bash
colcon build --packages-select com2009_team65_2025 --symlink-install
source ~/.bashrc
ros2 launch com2009_team65_2025 task3.launch.py target_colour:=COLOUR
```
where `COLOUR` is one of {red, green, blue, yellow}.

Make sure the robot is placed in the arena before running the last command.


## Functional Description

### Navigation and Exploration Strategy

The `exploration_controller.py` file implements a navigation strategy inspired by Levy flight, mimicking natural animal exploration. The robot moves in straight segments of random lengths followed by randomized turns. This results in broad, efficient coverage of the environment.

* Drives forward a random distance (0.3 m to 1.0 m)
* Rotates randomly between 45° and 180°
* If an obstacle is detected (< 0.25 m):

  * Stops
  * Reverses slightly (e.g., 5 cm)
  * Rotates to a clear direction based on LiDAR data

This reactive approach ensures effective area coverage in a time-limited scenario.

### Obstacle Avoidance

LiDAR provides 360° distance measurements. The robot monitors the forward sector for nearby obstacles:

* On detection:

  * Halts immediately
  * Reverses slightly
  * Scans for a direction with maximum clearance and rotates accordingly

This loop runs continuously for safe navigation.

### Zone Tracking

The arena is abstracted into a 3×3 grid. The robot uses odometry data to track its position and marks visited zones in a dictionary. This prevents redundant exploration and guides turn decisions.

## Beacon Detection and Photo Capture
In parallel with navigation, a dedicated ROS2 node named BeaconDetector runs continuously. This is defined in beacon_detector.py. This node subscribes to the /camera/image_raw topic and uses OpenCV to process incoming frames.

The detection pipeline consists of:

- Converting the RGB image to HSV colour space.
- Applying colour masking based on the user-defined target (i.e., red, blue, green, or yellow).
- Using the m00 image moment to detect if there is a minimum area of our target colour.
- Checking horizontal lines across the image, to ensure we haven't captured one solid block of colour (like a wall).
  - This feature is disabled in simulation, because it's not necessary in the low-noise environment.
- Once we think we have a real pillar, requesting control from the ExplorationController, and turning towards the centre of the block of colour.
- Once we're at the centre, taking a picture, handing control back to the ExplorationController, and shutting down the node.
- If at any point we lose sight of the pillar, hand back control, and set a cooldown, so that the BeaconDetector does not immediately request control again if it sees a false or intermittent signal.

### Control Sharing
The ExplorationController and BeaconDetector nodes both wish to move the robot around. We make use of a Service called ControlSharingReq to achieve this. The ExplorationController, which controls the robot the majority of the time, runs a control-sharing server. It also has a flag which prevents it from moving if set. When the BeaconDetector wants control of the robot, it sends a message to the ExplorationController. On receipt, a callback in the ExplorationController sets this flag, which suspends exploration until the BeaconDetector finishes its business, when it sends another message handing back control to the ExplorationController, which resets its flag and goes on with its business.


## SLAM and Map Saving
Simultaneously, the application runs Cartographer SLAM, a 2D mapping solution that combines LiDAR and odometry data through slam_mapper.py to incrementally build a representation of the environment. The map is published to the /map topic and can be viewed in real time using rviz2.

At the end of the 3-minute run (or upon a shutdown signal), the current map is saved as a PNG image with a YAML metadata file using the map_saver node. This map is stored under the /maps/ directory and named arena_map.png.

This functionality ensures that the robot not only explores the environment but also leaves behind a usable record of the space it covered.

![Functional Block Diagram](./functional_block_diagram.png)

## Contributors

* [Lottie McGhee](https://github.com/drearyplane8)
* [Tommy Sargaison](https://github.com/tommmicron)
* [Nurul Husna Mohmad Hakim](https://github.com/aca23nhm)
* [Nik Farhanah Nik Zawawi](https://github.com/anahnick)
