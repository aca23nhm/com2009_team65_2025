#!/usr/bin/env python3

import rclpy 
from rclpy.node import Node
from rcl_interfaces.msg import ParameterType

import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

import os
from geometry_msgs.msg import Twist 
from com2009_team65_2025.srv import ControlSharingReq
from ament_index_python.packages import get_package_share_directory

class BeaconDetector(Node):

    def __init__(self):
        super().__init__("beacon_detector")

        # Declare ROS2 parameters
        self.declare_parameter("target_colour", "yellow")
        self.target_colour = self.get_parameter("target_colour").get_parameter_value().string_value

        self.declare_parameter("in_simulator", True)
        self.in_simulator = self.get_parameter("in_simulator").get_parameter_value().bool_value
        self.get_logger().info(f"In simulator is {self.in_simulator}")
        
        # Set up pub/subs, client for control sharing.
        self.camera_sub = self.create_subscription(
            msg_type=Image,
            topic=f"/camera/image_raw",
            callback=self.camera_callback,
            qos_profile=10
        )

        self.vel_pub = self.create_publisher(
            msg_type=Twist,
            topic="/cmd_vel",
            qos_profile=10
        )

        # Start up the timer callback
        self.timer = self.create_timer(
            timer_period_sec=1/5,
            callback=self.centre_pillar_callback
        )        

        self.control_requester = self.create_client(
            ControlSharingReq, 'exploration_controller_control_controller'
        )

        # Stop the camera callback from being annoying if the centrer callback is running
        self.centering = False
        self.moments_for_turning = 0
        self.is_straight_ahead = False
        self.cooldown_after_losing = 0

        # constants
        self.LOSING_COOLDOWN_LEN = 5
        self.m00_MINIMUM = 100_000
        self.TURN_RATE = -0.1
        self.CENTRE_OFFSET = 25 # pixels from the centre that we can stop in center_callback

        self.package_dir = get_package_share_directory('com2009_team65_2025')
        self.waiting_for_image = True
        self.bridge = CvBridge()
        self.get_logger().info(f"TARGET BEACON: Searching for {self.target_colour}")

    def does_row_contain_zeroes(self, row, threshold=50):
        return len([px for px in row if px == 0]) > threshold
    
    def does_row_contain_ones(self, row, threshold=50):
        return len([px for px in row if px == 255]) > threshold

    def image_has_clear_areas(self, img, cz):
        height, w = img.shape
        self.get_logger().info(f"Height: {height}, width: {w}")

        check_points = [int(height * (0.25*x) - 1) for x in range(1, 4)]
        self.get_logger().info(f"Checkpoints at {[i for i in check_points]}")
        assert len(check_points) == 3
        
        rows = [img[p] for p in check_points]

        self.debug_img = img.copy()
        for z in check_points:
            cv2.line(self.debug_img, (0,z), (w, z), (255, 0, 0), 1)
        
        return any(map( self.does_row_contain_zeroes, rows)) and any(map( self.does_row_contain_ones, rows))

    def pass_data_to_centrer(self, moments, img):
        self.full_image = img
        self.moments_for_turning = moments

    def get_colour_thresholds(self):
        if self.target_colour == "blue":
            return (100, 100, 100), (130, 255, 255)
        elif self.target_colour == "red":
            return (0, 100, 100), (10, 255, 255)
        elif self.target_colour == "green":
            return (40, 100, 100), (80, 255, 255)
        elif self.target_colour == "yellow":
            return (20, 100, 100), (30, 255, 255)
        else:
            self.get_logger().warn(f"Unknown target colour: {self.target_colour}, defaulting to yellow.")
            return (20, 100, 100), (30, 255, 255)
        
    def camera_callback(self, img_data):

        try:
            cv_img = self.bridge.imgmsg_to_cv2(img_data, desired_encoding="bgr8")
        except CvBridgeError as e:
            self.get_logger().warning(f"{e}")
            return

        if self.waiting_for_image:
            height, width, _ = cv_img.shape
            #self.get_logger().info(f"Height: {height}, Width: {width} of original image")
            crop_width = int(width * 1)     # roughly equal to the absolute values from Ass1 Part6
            crop_height = int(height * 0.5)
            crop_y0 = int((width / 2) - (crop_width / 2))
            crop_z0 = 0
            cropped_img = cv_img[crop_z0:crop_z0+crop_height, crop_y0:crop_y0+crop_width]

            hsv_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2HSV)
            lower, upper = self.get_colour_thresholds()
            img_mask = cv2.inRange(hsv_img, lower, upper)

            moments = cv2.moments(img_mask)

            if self.centering:
                self.pass_data_to_centrer(moments, cv_img)
                return
            
            if moments['m00'] == 0:
                return
            
            cy = get_cy(moments)
            cz = get_cz(moments)

            clear_areas = self.image_has_clear_areas(img_mask, cz)

            if moments['m00'] > self.m00_MINIMUM and img_mask[cz, cy] == 255 and (self.in_simulator or clear_areas):
                
                # We have found something! lets try and turn towards it

                # Hand it the data it needs (moments, the full image to save)
                self.pass_data_to_centrer(moments, cv_img)

                # Send a request ot the main ExplorationController for control of the robot's movement
                self.send_control_req(False) # I would like control

                # Set the centerer off to the races
                self.centering = True

                cv2.circle(self.debug_img, (cy, cz), 10, (0, 0, 255), 2)

    
    def show_img(self, img, img_name, save_img=False): 
        self.get_logger().info("Opening the image in a new window...")
        cv2.imshow(img_name, img) 

        if save_img: 
            self.save_image(img, img_name)

        self.get_logger().info(
            "IMPORTANT: Close the image pop-up window to exit."
        )
        cv2.waitKey(0) 

    # Callback that handles turning in place to try and centre a beacon
    def centre_pillar_callback(self):
        if self.cooldown_after_losing > 0:
            self.get_logger().info(f"Cooling down after losing pillar, time remaining until we can turn again: {self.cooldown_after_losing}")
            self.cooldown_after_losing -= 1
            return

        if not self.centering:
            return

        cy = get_cy(self.moments_for_turning)
        m00 = self.moments_for_turning['m00']

        _, width, _ = self.full_image.shape
        centre = int(width / 2)


        # Check whether there is a blob worth stopping for
        if m00 > self.m00_MINIMUM: # TODO determine some good moo minima
            # blob detected - determine whether it is straight ahead or not
            self.is_straight_ahead = centre - self.CENTRE_OFFSET <= cy <= centre + self.CENTRE_OFFSET
        else:
            # We have lost sight of the blob, give up and try again
            self.get_logger().info("Lost sight of blob, giving up. ")
            self.stop_beacon_detecting()
            self.cooldown_after_losing = self.LOSING_COOLDOWN_LEN
            return
        
        if self.is_straight_ahead:
            self.get_logger().info(
                f"\nSTOPPED:\n"
                f"The blob of colour is now dead-ahead at y-position {cy:.0f} pixels. Snapping picture."
            )
            self.save_image(self.full_image)
            self.stop_beacon_detecting()
        else:
            self.get_logger().info(
                f"A blob of colour of size {m00:.0f} pixels is in view at y-position: {cy:.0f} pixels. Turning towards it."
            )
            vel_cmd = Twist()
            vel_cmd.angular.z = self.TURN_RATE * (-1 if cy < centre else 1)
            self.vel_pub.publish(vel_cmd)

    def stop_beacon_detecting(self):
        self.vel_pub.publish(Twist())
        self.centering = False
        self.send_control_req(True)

    def save_image(self, img, filename='target_beacon.jpg', debug=False):
        save_path = "/home/student/ros2_ws/src/com2009_team65_2025/snaps"
        
        os.makedirs(save_path, exist_ok=True)
        filename = os.path.join(save_path, filename)
        cv2.imwrite(filename, img)
        self.get_logger().info(f"Saved beacon snapshot to: {filename}") 

    def send_control_req(self, giving_back : bool):
        control_request = ControlSharingReq.Request()
        control_request.giving_back = giving_back
        self.control_requester.call_async(control_request)

def get_cy(moments, epsilon=1e-4):
    return int(moments['m10'] / (moments['m00'] + epsilon))

def get_cz(moments, epsilon=1e-4):
    return int(moments['m01'] / (moments['m00'] + epsilon))


def main(args=None):
    rclpy.init(args=args)
    node = BeaconDetector()
    while node.waiting_for_image:
        rclpy.spin_once(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
