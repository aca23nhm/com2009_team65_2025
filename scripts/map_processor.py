import rclpy
from rclpy import Node
from nav_msgs.msg import OccupancyGrid
from geometry_msgs.msg import Pose, PoseStamped

import numpy # array manipulation


class MapProcessor(Node):

  def __init__(self):
    self.map_sub = self.create_subscription(OccupancyGrid, '/map', self.map_received)


  def map_received(self, msg):
    print("time to process map data!")
    map_origin : Pose = msg.info.origin # useful information for corresponding map space to robot space?
    map_data = msg.data # byte array

    selected = 0
    for i in range(0, len(map_data)):
       if map_data[i] == -1: # if it is unexplored territory
          selected = i



  def map_index_to_coordinates(self, map, index):
    print("time to process the map!!")
    # we need to read the header data to work out how to do that 
    

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
