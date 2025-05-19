# Overview (A brief explanation of what your application does (no more than 100 words))
This ROS2 Python application enables a TurtleBot to autonomously explore an arena within 3 minutes and avoiding obstacles and building a coverage map and save it via SLAM. It uses LiDAR and odometry data to detect and navigate around obstacles while marking visited areas on a 3×3 grid. The robot moves in randomized segments with adaptive turning. Using ROS2 node BeaconDetector, it identifies coloured beacons using the robot's built-in camera. It captures a photo when the target colour is found and saves it locally. The system combines autonomous navigation, visual detection, and map generation for efficient environment exploration and documentation.

# Installation and Execution

This guide assumes ROS2 has been installed via [the University's Guide](https://tom-howard.github.io/com2009/ros/).

## Cloning the repository
To clone our repo, in `~/ros2_ws/src/`, run:

`git clone https://github.com/aca23nhm/com2009_team65_2025.git`.

This will install all our packages into your workspace ready to be run.

## Pairing the robot
This guide assumes you know how to do this.

## Running our navigation program

In a terminal, navigate to `~/ros2_ws/src` and run these commands:
`colcon build --packages-select com2009_team65_2025 --symlink-install`,

`source ~/.bashrc`, and

`ros2 launch com2009_team65_2025 task3.launch.py target_colour:=COLOUR`.

This last command starts the robot running, so make sure to place the robot in the arena
before this.

# Functional Description
The application enables a TurtleBot3 Waffle to autonomously explore a 4x4m arena within 3-minute. The robot builds a coverage map while avoiding collisions and capturing visual evidence of a coloured beacon.

## Navigation and Exploration Strategy
In exploration_controller.py, the robot uses a navigation strategy inspired by Levy flight, which mimics the natural movement patterns of animals exploring an unknown environment. This approach involves moving in straight segments of variable length followed by randomized turns. Over time, this results in broad and somewhat efficient area coverage.

The movement system operates as follows:

The robot drives forward a random distance within a bounded range (e.g., 0.3 m to 1.0 m).

After each segment, the robot rotates a random angle (e.g., between 45° and 180°).

If the robot detects an obstacle within a safety threshold (e.g., < 0.25 m), it immediately reverses slightly and rotates until a clear path is identified.

Turning directions are chosen based on the least obstructed heading using LiDAR scan data.

This method is not only simple and reactive, but also effective for covering space in time-limited scenarios.

## Obstacle Avoidance
Obstacle detection is handled using data from the robot’s LiDAR sensor. The 360° scan provides distance measurements to nearby objects. The robot continuously monitors the minimum distance in its forward-facing sector. If a potential collision is detected:

The robot halts immediately.

It reverses slightly (e.g., 5 cm).

It scans the environment and chooses a new heading that avoids the obstacle, using basic trigonometric evaluation of scan data to select the direction with the greatest clearance.

This process is repeated throughout the exploration, allowing the robot to safely maneuver around walls, boxes, and other structures.

## Zone Tracking
The arena is abstracted as a 3×3 grid. The robot updates a zone-tracking dictionary with its estimated (x, y) coordinates, transformed from odometry data. When a new zone is entered, it's marked as visited to avoid redundant navigation. This zone-awareness is used to guide turning decisions.

## Beacon Detection and Photo Capture
In parallel with navigation, a dedicated ROS2 node named BeaconDetector runs continuously. This is defined in beacon_detector.py. This node subscribes to the /camera/image_raw topic and uses OpenCV to process incoming frames.

The detection pipeline consists of:

- Converting the RGB image to HSV colour space.
- Applying colour masking based on the user-defined target (i.e., red, blue, green, or yellow).
- Using the m00 image moment to detect if there is a minimum area of our target colour.
- Checking horizontal lines across the image, to ensure we haven't captured one solid block of colour (like a wall).
- Once we think we have a real pillar, requesting control from the ExplorationController, and turning towards the centre of the block of colour.
- Once we're at the centre, taking a picture, handing control back to the ExplorationController, and shutting down the node.

## Control Sharing
The ExplorationController and BeaconDetector nodes both wish to move the robot around. We make use of a Service called ControlSharingReq to achieve this. The ExplorationController, which controls the robot the majority of the time runs a control-sharing server. It also has a flag which prevents it from moving if set. When the BeaconDetector wants control of the robot, it sends a message to the ExplorationController. On receipt, a callback in the ExplorationController sets this flag, which suspends exploration until the BeaconDetector finishes its business, when it sends another message handing back control to the ExplorationController, which resets its flag and goes on with its business.

## SLAM and Map Saving
Simultaneously, the application runs Cartographer SLAM, a 2D mapping solution that combines LiDAR and odometry data through slam_mapper.py to incrementally build a representation of the environment. The map is published to the /map topic and can be viewed in real time using rviz2.

At the end of the 3-minute run (or upon a shutdown signal), the current map is saved as a PNG image with a YAML metadata file using the map_saver node. This map is stored under the /maps/ directory and named arena_map.png.

This functionality ensures that the robot not only explores the environment but also leaves behind a usable record of the space it covered.

Functional Block Diagram

# Contributor (team members and link to github profile)
[Lottie McGhee](https://github.com/drearyplane8)
[Tommy Sargaison](https://github.com/tommmicron)
[Nurul Husna Mohmad Hakim](https://github.com/aca23nhm)
[Nik Farhanah Nik Zawawi](https://github.com/anahnick)