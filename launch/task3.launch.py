from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, ExecuteProcess
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import LifecycleNode
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

    # Start Cartographer SLAM
    cartographer_launch = ExecuteProcess(
        cmd=[
            'ros2', 'launch', 'turtlebot3_cartographer', 'cartographer.launch.py', 'use_sim_time:=false'
        ],
        output='log' 
    )

    map_saver_node = Node(
        package='nav2_map_server',
        executable='map_saver_server',
        name='map_saver',
        output='screen',
        parameters=[{
            'save_map_timeout': 2000.0,
            'free_thresh': 0.25,
            'occupied_thresh': 0.65,
            'use_sim_time': False
        }]
    )
    lifecycle_manager = Node(
        package='nav2_lifecycle_manager',
        executable='lifecycle_manager',
        name='lifecycle_manager_map_saver',
        output='screen',
        parameters=[{
            'use_sim_time': False,
            'autostart': True,
            'node_names': ['map_saver']
        }]
    )
    # Your nodes
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
        map_saver_node,
        lifecycle_manager,
        beacon_detector_node,
        slam_mapper_node,
        exploration_controller_node
    ])
