from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    target_colour_arg = DeclareLaunchArgument(
        'target_colour',
        description='The colour of the beacon to search for (yellow|red|green|blue).'
    )

    return LaunchDescription([
        target_colour_arg,
        Node(
            package='com2009_team65_2025',
            executable='beacon_detector.py',
            name='beacon_detector',
            output='screen',
            parameters=[{'target_colour': LaunchConfiguration('target_colour')}]
        ),

        Node(
            package='com2009_team65_2025',
            executable='slam_mapper.py',
            name='slam_mapper'
        ),

        Node(
            package='com2009_team65_2025',
            executable='exploration_controller.py',
            name='exploration_controller'
        ),

    ])
