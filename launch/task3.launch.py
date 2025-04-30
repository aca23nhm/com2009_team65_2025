from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch_ros.actions import Node

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    # Declare launch argument for target colour
    target_colour_arg = DeclareLaunchArgument(
        'target_colour',
        description='The colour of the beacon to search for (yellow|red|green|blue).'
    )

    # Get the path to the Cartographer launch file
    cartographer_launch_path = os.path.join(
        get_package_share_directory('tuos_simulations'),
        'launch',
        'cartographer.launch.py'
    )

    # Include the Cartographer SLAM launch file
    # The Cartographer file launches RVIZ - we could potentially switch it out for one that doesn't
    # but it also launches the cartographer which is very useful
    cartographer_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(cartographer_launch_path),
        launch_arguments={'use_sim_time': 'false'}.items()
    )

    # Define all nodes
    beacon_detector_node = Node(
        package='com2009_team65_2025',
        executable='beacon_detector.py',
        name='beacon_detector',
        output='screen',
        parameters=[{'target_colour': LaunchConfiguration('target_colour')}]
    )

    # Commenting this out with intent to replace it
    #slam_mapper_node = Node(
    #    package='com2009_team65_2025',
    #    executable='slam_mapper.py',
    #    name='slam_mapper'
    #)

    #exploration_controller_node = Node(
    #    package='com2009_team65_2025',
    #    executable='exploration_controller.py',
    #    name='exploration_controller'
    #)

    # Return all launch actions (excluding map saver)
    return LaunchDescription([
        target_colour_arg,
        cartographer_launch,
        beacon_detector_node,
    ])
