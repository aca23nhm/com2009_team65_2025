#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid
import cv2
import numpy as np

class SLAMMapper(Node):
    def __init__(self):
        super().__init__("slam_mapper")

        self.subscription = self.create_subscription(OccupancyGrid, '/map', self.map_callback, 10)

    def map_callback(self, msg):
        width = msg.info.width
        height = msg.info.height
        data = np.array(msg.data).reshape((height, width))
        img = np.zeros((height, width, 3), dtype=np.uint8)
        img[data == 0] = [255, 255, 255]
        img[data == 100] = [0, 0, 0]
        cv2.imwrite('maps/arena_map.png', img)


def main(args=None):
    rclpy.init(args=args)
    node = SLAMMapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()