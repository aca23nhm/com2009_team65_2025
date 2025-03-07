from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='com2009_team65_2025',
            executable='obstacle_avoidance.py',
            output='screen'
        )
    ])
