import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, LogInfo, ExecuteProcess
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Launch the Exploration Server node
        Node(
            package='com2009_team65_2025',  # Replace with the actual package name
            executable='object_detection.py',  # The name of the server executable
            output='screen',
            #parameters=[{'param_name': 'param_value'}],  # Add any parameters if needed
            #remappings=[('/camera/image_raw', '/your_camera_topic')]  # Remap topics if needed
        ),
        
    ])
