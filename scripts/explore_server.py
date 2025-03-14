#!/usr/bin/env python3

# Import the core Python libraries for ROS and to implement ROS Actions:
import rclpy
from rclpy.node import Node
from rclpy.action import ActionServer, GoalResponse, CancelResponse

# Import additional rclpy libraries for multithreading and shutdown
from rclpy.executors import MultiThreadedExecutor
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.signals import SignalHandlerOptions

# Import our package's action interface:
from com2009_team65_2025.action import Explore

# Import other key ROS interfaces that this server will use:
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan

# Import some other useful Python Modules
from math import sqrt, pow, sin, cos, pi
import numpy as np
from part5_actions_modules.tb3_tools import quaternion_to_euler
from enum import Enum

VELOCITY_PUB_RATE = 10 # Hz
LIDAR_SUB_RATE = 10
MAIN_TIMER_RATE = 10 
FEEDBACK_TIMER_RATE = 10

STOPPING_DISTANCE = 0.25

FWD_VELOCITY = 0.25
ANG_VELOCITY = 1

# we want to make sure the robot gets near the goal - because its an area and also its not 100% precise/accurate
TARGET_RADIUS_ALLOWANCE = 0.5 # metres

class State(Enum):
   NONE = 0
   MOVE_TOWARDS_TARGET = 1
   AVOID_OBSTACLE = 2


class ExploreServer(Node):

  def __init__(self):
    super().__init__("explore_server")

    # set up pub/subs
    self.vel_pub = self.create_publisher(Twist, "/cmd_vel", VELOCITY_PUB_RATE)
    self.lidar_sub = self.create_subscription(LaserScan, "/scan", self.lidar_callback, LIDAR_SUB_RATE)
    self.odom_sub = self.create_subscription(msg_type=Odometry, topic="odom", callback=self.odom_callback, qos_profile=10,)

    # set up timers - they are initialised in self.server_entry_point
    self.main_timer = 0
    self.feedback_timer = 0

    # initialise member variables
    self.pos_x = 0
    self.pos_y = 0
    self.lidar_reading = 0
    self.goal = 0
    self.shutdown = False

    self.state = State.NONE
    self.target_index = 0

    self.is_done = False 

    # set up Server
    self.actionserver = ActionServer(
        node=self, 
        action_type=Explore,
        action_name="explore",
        execute_callback=self.server_entry_point,
        callback_group=ReentrantCallbackGroup(),
        goal_callback=self.goal_callback,
        cancel_callback=self.cancel_callback)
    

  def goal_callback(self, goal : Explore.Goal):
    self.get_logger().info(f"Stopping distance: {goal.stopping_distance}, the xs are {goal.target_xs}, the ys are {goal.target_ys}")

    goal_ok = ( # todo add checks to make sure goals are in the 4x4 robot arena
        len(goal.target_xs) == len(goal.target_ys) and
        0.2 < goal.stopping_distance < 1)
    self.goal = goal
    
    if goal_ok:
       self.get_logger().info("Goal accepted")
    else:
       self.get_logger().warn("Goal rejected")
    return GoalResponse.ACCEPT if goal_ok else GoalResponse.REJECT


  def cancel_callback(self, goal):
    """
    A callback to trigger cancellation of the action
    """
    self.get_logger().info('Received a cancel request...')
    return CancelResponse.ACCEPT 
  
  def feedback_callback(self):
    feedback = Explore.Feedback()

    feedback.current_target_x = self.goal.request.target_xs[self.target_index]
    feedback.current_target_y = self.goal.request.target_ys[self.target_index]
    feedback.current_state = str(self.state)
    self.goal.publish_feedback(feedback)
  
  def odom_callback(self, odom_msg: Odometry):
        self.posx = odom_msg.pose.pose.position.x
        self.posy = odom_msg.pose.pose.position.y
        
        _, _, yaw = quaternion_to_euler(odom_msg.pose.pose.orientation)
        self.th_z = abs(yaw)

        self.await_odom = False

  # todo make this provide a look to the side
  # we could probably also come up with a better method than the average - it could lead to us clipping
  # things on the side (i think)
  def lidar_callback(self, scan_msg: LaserScan):
        """
        Callback for the /scan subscriber
        """
        left_20_deg = scan_msg.ranges[0:21]
        right_20_deg = scan_msg.ranges[-20:] 
        front = np.array(left_20_deg + right_20_deg) 

        filtered_slice = front[front != float("inf")]
        # this is changed from NaN to Infinity from the example, which is much sensibler because it makes less/greater than checks
        # work as expected. Otherwise the robot will stop if it cant see anything instead of moving forward.
        self.lidar_reading = filtered_slice.mean() if np.shape(filtered_slice)[0] > 0 else float("Infinity")
        self.await_lidar = False


  # Our states have two functions - one when we transition into that state and a callback that gets
  # called while we're in that state. If we were gonna make this extensible, we would maybe have a
  # function for when we exit the state too? 

  # also the robot moves backwards sometimes lol - need to code it so it always moves the way its facing

  def start_move_towards_target(self):    
    self.target_x = self.goal.request.target_xs[self.target_index]
    self.target_y = self.goal.request.target_ys[self.target_index]
    
    self.get_logger().info(f"Starting a move towards the target (f{self.target_x}, f{self.target_y})")

    self.vel_pub.publish(Twist()) # cancel all current movement

    vel_cmd = Twist() # send move command to move forward at a certain rate
    vel_cmd.linear.x = FWD_VELOCITY * cos(self.th_z)
    vel_cmd.linear.y = FWD_VELOCITY * sin(self.th_z)

    self.vel_pub.publish(vel_cmd)
    self.state = State.MOVE_TOWARDS_TARGET

  
  def move_towards_target(self):

    # Get the robot's current position:
    while self.await_odom or self.await_lidar:
        continue
    
    self.get_logger().info("In the move-towards-target callback")

    # if we are up against a wall, transition to the avoidance state
    if self.lidar_reading < STOPPING_DISTANCE:
      self.get_logger().info("We're up against a wall!")

    # if we reach the goal (or close enough to it) then set the target to a new goal
    if is_within_radius(self.target_x, self.target_y, self.pos_x, self.pos_y, TARGET_RADIUS_ALLOWANCE):
       self.get_logger().info("yipee we reached the goal")

  # we can't hot-swap the callback on the timer, so we use this function to decide which one 
  # to use depending on which state we're in.
  def callback_manager(self):
     match self.state:
        case State.NONE:
          self.get_logger().fatal("Not in any state!")
          # todo halt and catch fire
        case State.MOVE_TOWARDS_TARGET:
          self.move_towards_target()
        case State.AVOID_OBSTACLE:
          self.avoid_obstacle() # this callback isnt written yet

  # this is the server call-back
  def server_entry_point(self, goal):

    self.get_logger().info("Server entry point has been reached.")

    self.goal = goal
    self.create_timer( (1/MAIN_TIMER_RATE), self.callback_manager)
    self.create_timer(FEEDBACK_TIMER_RATE, self.feedback_callback)
    self.start_move_towards_target()

    # this line is a problem. based on the example servers, they have this block in a while-loop until the result is done.
    # but since we hand it off to callbacks, we don't need to block the main thread? which is better coding practice.
    # however, I don't think the callbacks actually are multithreaded? because blocking this with a while loop will
    # prevent them from ever executing. but i think there might be a way to make them execute multithreadedly? I read
    # about callback groups in the docs.
    return Explore.Result() 
  

def is_within_radius(target_x, target_y, x, y, radius):
  return sqrt(pow((target_x - x), 2) + pow((target_y - y), 2)) < radius # euclidian distance to circle around centre

def main(args=None):
    rclpy.init(args=args)
    server = ExploreServer()

    executor = MultiThreadedExecutor()
    executor.add_node(server)

    try:
        server.get_logger().info(
            "Starting the Server (shut down with Ctrl+C)"
        )
        executor.spin()
    except KeyboardInterrupt:
        server.get_logger().info(
            "Server shut down with Ctrl+C"
        )
    finally:
        server.destroy_node()
        rclpy.shutdown() 
if __name__ == '__main__':
    main()


