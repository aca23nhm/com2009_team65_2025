#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from rclpy.signals import SignalHandlerOptions

import cv2
from cv_bridge import CvBridge, CvBridgeError

from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
import os

class ColourSearch(Node):

    def __init__(self):
        super().__init__("colour_search")

        self.declare_parameter("target_colour", "blue")
        self.target_colour = self.get_parameter("target_colour").get_parameter_value().string_value

        self.camera_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.camera_callback,
            10
        )

        self.vel_pub = self.create_publisher(
            Twist,
            "/cmd_vel",
            10
        )

        self.timer = self.create_timer(
            1/5,
            self.timer_callback
        )

        self.cvbridge_interface = CvBridge()

        self.turn_vel_fast = -0.5
        self.vel_cmd = Twist()
        self.m00_min = 10000
        self.m00 = 0
        self.cy = 0
        self.center_x = 560
        self.tolerance = 100

        self.image_captured = False
        self.current_image = None

        # Ensure snapshot directory exists
        self.package_dir = get_package_share_directory('com2009_team65_2025')
        self.get_logger().info(f"TARGET BEACON: Searching for {self.target_colour.upper()}")

    def get_colour_thresholds(self):
        if self.target_colour == "blue":
            return (80, 100, 50), (125, 255, 255)
        elif self.target_colour == "red":
            return (0, 100, 50), (15, 255, 255)
        elif self.target_colour == "green":
            return (74, 150, 50), (90, 255, 255)
        elif self.target_colour == "yellow":
            return (20, 120, 50), (30, 255, 255)
        else:
            self.get_logger().warn(f"Unknown colour '{self.target_colour}', defaulting to blue.")
            return (80, 100, 50), (125, 255, 255)

    def shutdown_ops(self):
        self.get_logger().info("Shutting down node...")
        cv2.destroyAllWindows()
        for _ in range(5):
            self.vel_pub.publish(Twist())

    def camera_callback(self, img_data):
        try:
            cv_img = self.cvbridge_interface.imgmsg_to_cv2(img_data, desired_encoding="bgr8")
            self.current_image = cv_img.copy()
        except CvBridgeError as e:
            self.get_logger().warn(f"{e}")
            return

        height, width, _ = cv_img.shape
        crop_width = width - 800
        crop_height = 400
        crop_x = int((width / 2) - (crop_width / 2))
        crop_y = int((height / 2) - (crop_height / 2))

        crop_img = cv_img[crop_y:crop_y+crop_height, crop_x:crop_x+crop_width]
        hsv_img = cv2.cvtColor(crop_img, cv2.COLOR_BGR2HSV)

        lower, upper = self.get_colour_thresholds()
        mask = cv2.inRange(hsv_img, lower, upper)

        m = cv2.moments(mask)
        self.m00 = m['m00']
        self.cy = int(m['m10'] / (m['m00'] + 1e-5))

        if self.m00 > self.m00_min:
            cv2.circle(crop_img, (self.cy, 200), 10, (0, 0, 255), 2)

        cv2.imshow('Beacon Detection', crop_img)
        cv2.waitKey(1)

    def timer_callback(self):
        twist = Twist()

        if self.m00 > self.m00_min and not self.image_captured:
            if abs(self.cy - self.center_x) <= self.tolerance:
                self.get_logger().info(f"✔ Beacon centered at {self.cy} — capturing image.")
                twist.angular.z = 0.0
                self.capture_image()
                self.image_captured = True
            elif self.cy < self.center_x - self.tolerance:
                twist.angular.z = 0.1  # turn right
            elif self.cy > self.center_x + self.tolerance:
                twist.angular.z = -0.1  # turn left
        else:
            twist.angular.z = 0.0  # stay still if no beacon or image already taken

        self.vel_pub.publish(twist)

    def capture_image(self):
        if self.current_image is not None:
            path = "/home/student/ros2_ws/src/com2009_team65_2025/snaps"
            os.makedirs(path, exist_ok=True)
            filename = os.path.join(path, "target_beacon.jpg")
            cv2.imwrite(filename, self.current_image)
            self.get_logger().info(f"Image saved to {path}")
        else:
            self.get_logger().warn(" Tried to capture image but current_image is None.")
    

def main(args=None):
    rclpy.init(args=args, signal_handler_options=SignalHandlerOptions.NO)
    node = ColourSearch()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        node.get_logger().info("Shutdown requested (Ctrl+C).")
    finally:
        node.shutdown_ops()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
