#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from nav_msgs.msg import OccupancyGrid, MapMetaData
from geometry_msgs.msg import Pose, PoseStamped
from random import randrange

import numpy # array manipulation


class MapProcessor(Node):

  def __init__(self):

    super().__init__('map_processor')

    self.map_sub = self.create_subscription(OccupancyGrid, '/map', self.map_received, 1)
    self.goal_pose_pub = self.create_publisher(PoseStamped, '/goal_pose', 1)

    self.sent = False

  def map_received(self, msg):

    if self.sent:
      return

    self.get_logger().info("time to process map data!")
    map_data : list[int] = msg.data # array of signed bytes - python bindings treat as ints

    # randomly choose points within the map until we find one that is unexplored
    while map_data[point := randrange(0, msg.info.width * msg.info.height)] == -1: continue

    # get the coordinates of the point
    coords = self.map_index_to_coordinates(msg.info, point)
    self.get_logger().info(f'Target coordinates selected: {coords}')
    self.publish_goal_pose(*coords)
    
       
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

def main(args=None):
    rclpy.init(args=args)
    node = MapProcessor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
