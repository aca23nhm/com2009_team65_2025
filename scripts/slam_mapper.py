#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav2_msgs.srv import SaveMap
from std_msgs.msg import Bool
import os
import time

class SLAMMapper(Node):
    def __init__(self):
        super().__init__("slam_mapper")

        self.maps_dir = '/home/student/ros2_ws/src/com2009_team65_2025/maps'
        os.makedirs(self.maps_dir, exist_ok=True)

        self.save_map_client = self.create_client(SaveMap, '/map_saver/save_map')

        self.done_subscription = self.create_subscription(
            Bool,
            '/exploration_done',
            self.exploration_done_callback,
            10
        )

    def exploration_done_callback(self, msg):
        if msg.data:
            self.get_logger().info("Exploration complete. Attempting to save map...")

            if not self.save_map_client.wait_for_service(timeout_sec=60.0):
                self.get_logger().warn("❌ /map_saver/save_map service is not available.")
                return

            map_base_path = os.path.join(self.maps_dir, 'arena_map')
            request = SaveMap.Request()
            request.map_url = map_base_path
            request.image_format = 'png'
            request.free_thresh = 0.25
            request.occupied_thresh = 0.65

            future = self.save_map_client.call_async(request)
            rclpy.spin_until_future_complete(self, future, timeout_sec=30.0)

            # Check if files were actually created
            time.sleep(1.0)  # Brief delay to ensure files are written
            yaml_file = f"{map_base_path}.yaml"
            png_file = f"{map_base_path}.png"
            
            if os.path.exists(yaml_file) and os.path.exists(png_file):
                self.get_logger().info(f"✅ Map saved successfully (verified files exist)")
                self.get_logger().info(f"  - {yaml_file}")
                self.get_logger().info(f"  - {png_file}")
            else:
                self.get_logger().warn("❌ Map files not found after save attempt")
                if not os.path.exists(yaml_file):
                    self.get_logger().warn(f"  - Missing: {yaml_file}")
                if not os.path.exists(png_file):
                    self.get_logger().warn(f"  - Missing: {png_file}")

def main(args=None):
    rclpy.init(args=args)
    node = SLAMMapper()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()