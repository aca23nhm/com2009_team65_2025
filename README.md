# TurtleBot Autonomous Explorer

## Overview

This ROS2 Python application enables a TurtleBot to autonomously explore an arena within 3 minutes, avoiding obstacles and building a coverage map via SLAM. It uses LiDAR and odometry data to detect and navigate around obstacles while marking visited areas on a 3×3 grid. The robot moves in randomized segments with adaptive turning. Using the ROS2 node `BeaconDetector`, it identifies coloured beacons using the robot's built-in camera. A photo is captured and saved locally when the target colour is detected. The system combines autonomous navigation, visual detection, and map generation for efficient environment exploration and documentation.

## Installation and Execution

This guide assumes ROS2 has been installed via [the University's Guide](https://tom-howard.github.io/com2009/ros/).

### Cloning the Repository

To clone our repository, navigate to `~/ros2_ws/src/` and run:

```bash
git clone https://github.com/aca23nhm/com2009_team65_2025.git
```

This will install all our packages into your workspace ready to be run.

### Pairing the Robot

This guide assumes you are already familiar with the robot pairing process.

### Running the Navigation Program

Navigate to `~/ros2_ws/src` in a terminal and run the following commands:

```bash
colcon build --packages-select com2009_team65_2025 --symlink-install
source ~/.bashrc
ros2 launch com2009_team65_2025 task3.launch.py target_colour:=COLOUR
```

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

### Beacon Detection and Photo Capture

The `BeaconDetector` node runs in parallel to navigation via `beacon_detector.py`. It subscribes to `/camera/image_raw` and processes images using OpenCV:

* Converts RGB to HSV
* Applies colour masking for the target (red, blue, green, yellow)
* Detects contours and bounding boxes
* Identifies the largest matching blob
* Validates beacon presence based on size and location

Once a valid beacon is centered in view, an image is saved as `snaps/target_beacon.jpg`, and detection halts.

### SLAM and Map Saving

SLAM is handled via Cartographer in `slam_mapper.py`:

* LiDAR and odometry data build a real-time 2D map
* The map is published to `/map` and visualised in `rviz2`
* At the 3-minute mark or shutdown:

  * The map is saved as `maps/arena_map.png`
  * A corresponding YAML file is generated

This feature ensures a persistent record of explored areas.

## Functional Block Diagram

(*Insert image or diagram here if applicable*)

## Contributors

* [Lottie McGhee](https://github.com/drearyplane8)
* [Tommy Sargaison](https://github.com/tommmicron)
* [Nurul Husna Mohmad Hakim](https://github.com/aca23nhm)
* [Nik Farhanah Nik Zawawi](https://github.com/anahnick)
