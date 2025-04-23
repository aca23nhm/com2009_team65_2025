#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist

import os
from pathlib import Path
from ament_index_python.packages import get_package_share_directory

class BeaconDetector(Node):

    def __init__(self):
        super().__init__("beacon_detector")

        self.declare_parameter("target_colour", "yellow")
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

        self.package_dir = get_package_share_directory('com2009_team65_2025')
        self.bridge = CvBridge()
        self.waiting_for_alignment = True
        self.snapshot_taken = False

        # Centroid alignment settings
        self.target_cy_range = (460, 660)
        self.turn_vel_fast = -0.5
        self.turn_vel_slow = -0.1

        self.get_logger().info(f"TARGET BEACON: Searching for {self.target_colour}")

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
            self.get_logger().warn(f"Unknown target colour: {self.target_colour}, defaulting to yellow.")
            return (20, 120, 50), (30, 255, 255)

    def camera_callback(self, img_data):
        try:
            cv_img = self.bridge.imgmsg_to_cv2(img_data, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().warning(f"{e}")
            return

        height, width, _ = cv_img.shape
        crop_width = width - 400
        crop_height = 400
        crop_y0 = int((width / 2) - (crop_width / 2))
        crop_z0 = int((height / 2) - (crop_height / 2))
        cropped_img = cv_img[crop_z0:crop_z0+crop_height, crop_y0:crop_y0+crop_width]

        hsv_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
        lower, upper = self.get_colour_thresholds()
        img_mask = cv2.inRange(hsv_img, lower, upper)

        moments = cv2.moments(img_mask)
        m00 = moments['m00']

        if m00 > 10000:
            cy = int(moments['m10'] / m00)
            cz = int(moments['m01'] / m00)
            filtered_img = cv2.bitwise_and(cropped_img, cropped_img, mask=img_mask)
            cv2.circle(filtered_img, (cy, cz), 10, (0, 0, 255), 2)

            # Decide movement
            twist = Twist()
            if cy < self.target_cy_range[0]:
                self.get_logger().info("Beacon on the right - turning right.")
                twist.angular.z = self.turn_vel_fast
            elif cy > self.target_cy_range[1]:
                self.get_logger().info("Beacon on the left - turning left.")
                twist.angular.z = -self.turn_vel_fast
            else:
                self.get_logger().info("Beacon centered - taking snapshot.")
                twist.angular.z = 0.0
                self.vel_pub.publish(twist)

                if not self.snapshot_taken:
                    self.save_snapshot(cropped_img)
                    self.snapshot_taken = True
                    self.waiting_for_alignment = False

            self.vel_pub.publish(twist)

    def save_snapshot(self, img):
        save_path = "/home/student/ros2_ws/src/com2009_team65_2025/snaps"
        os.makedirs(save_path, exist_ok=True)
        filename = os.path.join(save_path, "target_beacon.jpg")
        cv2.imwrite(filename, img)
        self.get_logger().info(f"Saved beacon snapshot to: {filename}")
        cv2.destroyAllWindows()

def main(args=None):
    rclpy.init(args=args)
    node = BeaconDetector()
    while node.waiting_for_alignment:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
