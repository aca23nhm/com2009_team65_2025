#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

import os
from pathlib import Path
from math import atan
from ament_index_python.packages import get_package_share_directory

class BeaconDetector(Node):

    def __init__(self):
        super().__init__("beacon_detector")

        self.declare_parameter("target_colour", "yellow")
        self.target_colour = self.get_parameter("target_colour").get_parameter_value().string_value
        
        self.camera_sub = self.create_subscription(
            msg_type=Image,
            topic="/camera/color/image_raw",
            callback=self.camera_callback,
            qos_profile=10
        )
        
        self.package_dir = get_package_share_directory('com2009_team65_2025')
        self.waiting_for_image = True
        self.bridge = CvBridge()
        self.get_logger().info(f"TARGET BEACON: Searching for {self.target_colour}")

    def does_row_contain_zeroes(self, row, threshold=50):
        return len([px for px in row if px == 0]) > threshold
    
    def does_row_contain_ones(self, row, threshold=50):
        return len([px for px in row if px == 255]) > threshold

    def image_has_clear_areas(self, img, cz):
        SCALE_FACTOR = 0.5
        img = cv2.resize(img, (0,0), fx=SCALE_FACTOR, fy=SCALE_FACTOR)
        height, w = img.shape
        self.get_logger().info(f"Height: {height}, width: {w}")
        cz *= SCALE_FACTOR

        check_points = [int(height * (0.25*x) - 1) for x in range(1, 4)]
        self.get_logger().info(f"Checkpoints at {[i for i in check_points]}")
        assert len(check_points) == 3
        
        rows = [img[p] for p in check_points]

        self.debug_img = img.copy()
        for z in check_points:
            cv2.line(self.debug_img, (0,z), (w, z), (255, 0, 0), 1)
        
        return any(map( self.does_row_contain_zeroes, rows)) and any(map( self.does_row_contain_ones, rows))

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

        if self.waiting_for_image:
        
            self.show_img(cv_img, "original")
        
            height, width, _ = cv_img.shape
            self.get_logger().info(f"Height: {height}, Width: {width} of original image")
            crop_width = width - 400
            crop_height = 400
            crop_y0 = int((width / 2) - (crop_width / 2))
            crop_z0 = 0
            cropped_img = cv_img[crop_z0:crop_z0+crop_height, crop_y0:crop_y0+crop_width]
            self.show_img(cropped_img, "cropped")


            hsv_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
            lower, upper = self.get_colour_thresholds()
            img_mask = cv2.inRange(hsv_img, lower, upper)

            moments = cv2.moments(img_mask)
            if moments['m00'] == 0:
                self.get_logger().info("Stopping image processing here because m00 is zero.")
                return
            cy = int(moments['m10'] / moments['m00'])
            cz = int(moments['m01'] / moments['m00'])

            clear_areas = self.image_has_clear_areas(img_mask, cz)
            self.get_logger().info(f"This image has clear areas: {clear_areas}")
            self.get_logger().info(f"White area in this image: {moments['m00']}.")
            if moments['m00'] > 400000 and clear_areas and img_mask[cy, cz] == 255 or True:
                
                cv2.circle(self.debug_img, (cy, cz), 10, (0, 0, 255), 2)
                self.show_img(self.debug_img, "lines")


                # Save snapshot - modified path
                save_path = "/home/student/ros2_ws/src/com2009_team65_2025/snaps"
                
                os.makedirs(save_path, exist_ok=True)
                filename = os.path.join(save_path, "target_beacon.jpg")
                cv2.imwrite(filename, cropped_img)
                self.get_logger().info(f"Saved beacon snapshot to: {filename}")

                self.waiting_for_image = False
                cv2.destroyAllWindows()    
    
    def show_img(self, img, img_name, save_img=False): 
        self.get_logger().info("Opening the image in a new window...")
        cv2.imshow(img_name, img) 

        if save_img: 
            self.save_image(img, img_name)

        self.get_logger().info(
            "IMPORTANT: Close the image pop-up window to exit."
        )
        cv2.waitKey(0) 




def main(args=None):
    rclpy.init(args=args)
    node = BeaconDetector()
    while node.waiting_for_image:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()