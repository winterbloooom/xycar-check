#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy, math
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker, MarkerArray
from std_msgs.msg import ColorRGBA
from geometry_msgs.msg import Point, Vector3

class LineStrip:
    def __init__(self, id, p2):
        self.mark = Marker()
        self.mark.header.frame_id = '/laser' #map'
        self.mark.ns = "angle"
        self.mark.id = id
        self.mark.type = Marker.LINE_STRIP
        self.mark.action = Marker.ADD
        self.mark.color = ColorRGBA(1, 1, 1, 1)
        self.mark.scale.x = 0.02
        self.mark.pose.orientation.w = 1        
        self.mark.points.append(Point(0, 0, 0))
        self.mark.points.append(Point(p2[0], p2[1], 0))

class Text:
    def __init__(self, id, text, pose):
        self.mark = Marker()
        self.mark.header.frame_id = '/laser' #map'
        self.mark.ns = "text"
        self.mark.id = id
        self.mark.type = Marker.TEXT_VIEW_FACING
        self.mark.action = Marker.ADD
        self.mark.color = ColorRGBA(1, 1, 1, 1)
        self.mark.scale.z = 0.4
        self.mark.text = text
        self.mark.pose.position = Point(pose[0], pose[1], 0.1)

# ranges = []
# angle_min = 0
# angle_max = 0
# angle_increment = 0

# def callback(msg):
#     global ranges, angle_min, angle_max, angle_increment
#     ranges = msg.ranges
#     angle_min = msg.angle_min
#     angle_max = msg.angle_max
#     angle_increment = msg.angle_increment

rospy.init_node('lidar_test', anonymous=False)
# rospy.Subscriber("/scan", LaserScan, callback, queue_size=1)
pub = rospy.Publisher("/lidar_rviz", MarkerArray, queue_size=10)

rate = rospy.Rate(10)

while not rospy.is_shutdown():
    markers = MarkerArray()
    for angle in range(0, 361, 30):
        p2 = [2 * math.cos(math.radians(angle)),\
              2 * math.sin(math.radians(angle))]
        p2_txt = [2.3 * math.cos(math.radians(angle)),\
                  2.3 * math.sin(math.radians(angle))]
        line = LineStrip(angle, p2)
        text = Text(angle+1, str(angle), p2_txt)
        markers.markers.append(line.mark)
        markers.markers.append(text.mark)
    pub.publish(markers)
    rate.sleep()