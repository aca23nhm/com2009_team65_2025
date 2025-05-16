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

        self.declare_parameter("in_simulator", False)
        self.in_simulator = self.get_parameter("in_simulator").get_parameter_value().bool_value
        self.get_logger().info(f"In simulator is {self.in_simulator}")
        
        # Set up pub/subs, client for control sharing.
        self.camera_sub = self.create_subscription(
            msg_type=Image,
            topic=f"/camera/{'color/' if not self.in_simulator else ''}image_raw",
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
            ControlSharingReq, 'beacon_detector'
        )

        # timer callback uses this
        self.stop_counter = 0

        # Stop the camera callback from being annoying if the centrer callback is running
        self.centering = False
        self.moments_for_turning = 0
        self.move_rate = ''

        # constants
        self.m00_MINIMUM = 0
        self.FAST_TURN_RATE = -0.5 # Values from tuos_simulations/colour_search
        self.SLOW_TURN_RATE = -0.1
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
        

        
            height, width, _ = cv_img.shape
            #self.get_logger().info(f"Height: {height}, Width: {width} of original image")
            crop_width = int(width * 1)     # roughly equal to the absolute values from Ass1 Part6
            crop_height = int(height * 0.375)
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
            self.get_logger().info(f"This image has clear areas: {clear_areas}")
            self.get_logger().info(f"White area in this image: {moments['m00']}.")
            if moments['m00'] > 400000 and clear_areas and img_mask[cz, cy] == 255:
                
                # We have found something! lets try and turn towards it

                # Hand it the data it needs (moments, the full image to save)
                self.pass_data_to_centrer(moments, cv_img)

                # Send a request ot the main ExplorationController for control of the robot's movement
                control_request = ControlSharingReq.Request()
                control_request.giving_back = False
                self.control_requester.call_async(control_request)

                # Set the centerer off to the races
                self.centering = True

                cv2.circle(self.debug_img, (cy, cz), 10, (0, 0, 255), 2)
                if not self.in_simulator or True:
                    self.save_image(cv_img, filename="original.jpg", debug=True)
                    self.save_image(cropped_img, "cropped.jpg", debug=True)
                    self.save_image(img_mask, 'img_mask.jpg', debug=True)
                    self.save_image(self.debug_img, filename='lines_centroid.jpg', debug=True)

    
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
    # TODO why is its movement so jittery? probably cos of time to process 1080p image
    def centre_pillar_callback(self):
        if not self.centering:
            return
        
        if self.stop_counter > 0:
            self.stop_counter -= 1

        cy = get_cy(self.moments_for_turning)
        m00 = self.moments_for_turning['m00']
        vel_cmd = Twist()

        height, width, _ = self.full_image.shape
        centre = int(width / 2)

        # I think the m00 minima need to be much higher - see the funny picture
        if m00 > 400000: # TODO determine some good moo minima
            # blob detected
            if centre - self.CENTRE_OFFSET <= cy <= centre + self.CENTRE_OFFSET:
                if self.move_rate == 'slow':
                    self.move_rate = 'stop'
                    self.stop_counter = 15
            else:
                self.move_rate = 'slow'
        else:
            self.move_rate = 'fast'
            
        if self.move_rate == 'fast':
            self.get_logger().info(
                "\nMOVING FAST:\n"
                "I can't see anything at the moment, scanning the area..."
            )
            vel_cmd.angular.z = self.FAST_TURN_RATE * (-1 if cy < centre else 1)
            
        elif self.move_rate == 'slow':
            self.get_logger().info(
                f"\nMOVING SLOW:\n"
                f"A blob of colour of size {m00:.0f} pixels is in view at y-position: {cy:.0f} pixels."
            )
            vel_cmd.angular.z = self.SLOW_TURN_RATE * (-1 if cy < centre else 1)
        
        elif self.move_rate == 'stop' and self.stop_counter > 0:
            self.get_logger().info(
                f"\nSTOPPED:\n"
                f"The blob of colour is now dead-ahead at y-position {cy:.0f} pixels... Counting down: {self.stop_counter}"
            )
            vel_cmd.angular.z = 0.0
            self.centering = False
            cv2.line(self.full_image, (cy, 0), (cy, height), (255, 0, 255), 1 ) # draw a line through the centroid
            self.save_image(self.full_image)
        
        else:
            self.get_logger().info(
                f"\nMOVING SLOW:\n"
                f"A blob of colour of size {m00:.0f} pixels is in view at y-position: {cy:.0f} pixels."
            )
            vel_cmd.angular.z = self.SLOW_TURN_RATE
        
        self.vel_pub.publish(vel_cmd)

    def save_image(self, img, filename='target_beacon.jpg', debug=False):
        save_path = "/home/student/ros2_ws/src/com2009_team65_2025/snaps" + ('/debug' if debug else '')
        
        os.makedirs(save_path, exist_ok=True)
        filename = os.path.join(save_path, filename)
        cv2.imwrite(filename, img)
        self.get_logger().info(f"Saved beacon snapshot to: {filename}")

        if not debug:
            self.waiting_for_image = False
            cv2.destroyAllWindows()    

# we need to adapt the cy to the full FOV coordinate system? to get it to line up properly????
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