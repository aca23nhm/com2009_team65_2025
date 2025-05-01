#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid, MapMetaData, Odometry
from geometry_msgs.msg import Pose, PoseStamped

from random import randrange
from math import sqrt



class MapProcessor(Node):

  def __init__(self):

    super().__init__('map_processor')

    self.map_sub = self.create_subscription(OccupancyGrid, '/map', self.map_received, 1)
    self.goal_pose_pub = self.create_publisher(PoseStamped, '/goal_pose', 1)
    self.odom_sub = self.create_subscription(Odometry, '/odom', self.odom_callback, 10)

    self.sent = False
    self.pose = 0

  def odom_callback(self, msg):
    self.pose = msg.pose.pose

  def map_received(self, msg):

    if self.sent:
      return

    self.get_logger().info("time to process map data!")
    map_data : list[int] = msg.data # array of signed bytes - python bindings treat as ints


    map_data_new = []
    # map all points to robot space
    for i in range(0, len(map_data)):
       map_data_new.append(self.map_index_to_coordinates(msg.info, i) if map_data[i] > 0 else -1)
    map_data = map_data_new

    # filter out all unexplored points, all points that are obstacles
    map_data = filter((lambda x : x != -1), map_data)

    # sort by euclidian distance to robot
    own_pos = (self.pose.position.x, self.pose.position.y)
    furthest = max(map_data, key = (lambda p : self.euclidian_distance(own_pos, p)))

    self.publish_goal_pose(*furthest)
    
    
       
  def publish_goal_pose(self, goal_x : int, goal_y : int):
    pose : PoseStamped = PoseStamped()
    pose.pose.position.x = goal_x
    pose.pose.position.z = goal_y

    if not self.sent:
      self.get_logger().info(f'Sending coordinates {goal_x}, {goal_y}')
      self.goal_pose_pub.publish(pose)
      self.sent = True


  def map_index_to_coordinates(self, info : MapMetaData, index : int):
    # first convert the flat index into a 2D index
    y = index / info.width
    x = index % info.width

    # then convert into coordinates centred on the map origin
    map_x = info.origin.position.x + (x * info.resolution)
    map_y = info.origin.position.z + (y * info.resolution)

    return (map_x, map_y)
    

  def trim_outside_area(self, map):
     return map # how the hell are we gonna do this?

  def euclidian_distance(self, p1 : tuple[float, float], p2 : tuple[float, float]):
    return sqrt(
      pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2)
    )

def main(args=None):
    rclpy.init(args=args)
    node = MapProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
