#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
from std_msgs.msg import Bool
import numpy as np
import yaml
import os
import cv2

class SLAMMapper(Node):
    def __init__(self):
        super().__init__("slam_mapper")

        # Subscribers
        self.subscription = self.create_subscription(
            OccupancyGrid,
            '/map',
            self.map_callback,
            100
        )

        self.done_subscription = self.create_subscription(
            Bool,
            '/exploration_done',
            self.exploration_done_callback,
            10
        )

        self.latest_map = None
        self.exploration_done = False

        # Set the path to the maps directory (using the path you specified)
        self.maps_dir = '/home/student/ros2_ws/src/com2009_team65_2025/maps'
        os.makedirs(self.maps_dir, exist_ok=True)

    def map_callback(self, msg):
        self.latest_map = msg

    def exploration_done_callback(self, msg):
        if msg.data and self.latest_map:
            self.get_logger().info("Exploration complete. Saving map...")
            self.save_map(self.latest_map)

    def save_map(self, msg):
        # Convert occupancy grid data to image
        width = msg.info.width
        height = msg.info.height
        data = np.array(msg.data).reshape((height, width))
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[data == 0] = [255, 255, 255]      # Free
        img[data == 100] = [0, 0, 0]          # Occupied
        img[data == -1] = [128, 128, 128]     # Unknown

        # Save as PNG
        png_path = os.path.join(self.maps_dir, 'arena_map.png')
        cv2.imwrite(png_path, img)

        # Save YAML metadata
        yaml_path = os.path.join(self.maps_dir, 'arena_map.yaml')
        map_metadata = {
            'image': 'arena_map.png',
            'resolution': msg.info.resolution,
            'origin': [
                msg.info.origin.position.x,
                msg.info.origin.position.y,
                0.0
            ],
            'negate': 0,
            'occupied_thresh': 0.65,
            'free_thresh': 0.196
        }

        with open(yaml_path, 'w') as file:
            yaml.dump(map_metadata, file)

        self.get_logger().info(f"Map saved to {png_path} and {yaml_path}")


def main(args=None):
    rclpy.init(args=args)
    node = SLAMMapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
