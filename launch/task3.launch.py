from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, ExecuteProcess
from launch.substitutions import LaunchConfiguration, boolean_substitution
from launch_ros.actions import Node
import os

def generate_launch_description():
    target_colour_arg = DeclareLaunchArgument(
        'target_colour',
        description='The colour of the beacon to search for (yellow|red|green|blue).'
    )

    in_simulator_arg = DeclareLaunchArgument(
        'in_simulator',
        default_value='False',
        description='Boolean value - are we running in the simulator or not?'
    )

    cartographer_launch = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'tuos_simulations', 'cartographer.launch.py', 'use_sim_time:=false'
        ],
        output='log' 
    )

    beacon_detector_node = Node(
        package='com2009_team65_2025',
        executable='beacon_detector.py',
        name='beacon_detector',
        output='screen',
        parameters=[{'target_colour': LaunchConfiguration('target_colour'), 'in_simulator': LaunchConfiguration('in_simulator')}] # TODO: add as actual param
    )

    slam_mapper_node = Node(
        package='com2009_team65_2025',
        executable='slam_mapper.py',
        name='slam_mapper'
    )

    exploration_controller_node = Node(
        package='com2009_team65_2025',
        executable='exploration_controller.py',
        name='exploration_controller'
    )

    return LaunchDescription([
        target_colour_arg,
        in_simulator_arg,
        cartographer_launch,
        beacon_detector_node,
        slam_mapper_node,
        exploration_controller_node
    ])
