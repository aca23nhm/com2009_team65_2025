from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='com2009_team65_2025',
            executable='explore_forward_server.py',
            output='screen'
        ),
        Node(
            package='com2009_team65_2025',
            executable='explore_forward_client.py',
            output='screen'
        )
    ])
