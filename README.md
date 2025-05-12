# Overview (A brief explanation of what your application does (no more than 100 words))
Our program intends to successfully navigate a TurtleBot around a small arena, exploring unexplored
areas and taking pictures of coloured cyinders with the built-in camera. 

TODO add details

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
`colcon build --packages-select com2009_team65_2025`,

`source ~/.bashrc`, and

`ros2 launch com2009_team65_2025 task3.launch.py`.

This last command starts the robot running, so make sure to place the robot in the arena
before this.

# Functional Description
For navigation, we intended to use the `nav2` interface to build a map of the area with the Lidar
sensor and use it to pathfind a way to the nearest unexplored area. This proved challenging to
implement, so a more traditional approach was used. 

The robot is programmed to move in a manner similar to Levy flight, with it driving in a straight
line for a variable distance before turning. In open areas the straight segments and rotations are
semi-randomised, but when the robot detects an obstacle nearby it intelligently backs up and finds
a safe direction to rotate to.

The robot keeps track of the areas it has visited

TODO Functional Block Diagram

# Contributor (team members and link to github profile)
- [Lottie McGhee](https://github.com/drearyplane8)
- [Tommy Sargaison](https://github.com/tommmicron)
- [Nurul Husna Mohmad Hakim](https://github.com/aca23nhm)
- [Nik Farhanah Nik Zawawi](https://github.com/anahnick)