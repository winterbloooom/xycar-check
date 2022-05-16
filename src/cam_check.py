#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

image = None
bridge = CvBridge()

def img_callback(msg):
    global image, bridge
    image = bridge.imgmsg_to_cv2(msg, "bgr8")

rospy.init_node('cam_test', anonymous=False)
rospy.Subscriber("/usb_cam/image_raw/", Image, img_callback)

rate = rospy.Rate(10)

while cv2.waitKey(1) != 27: #not rospy.is_shutdown():
    for row in range(20, 481, 20):
        # TODO 글자 위치 조정
        cv2.putText(image, row, (2, row + 5), color=(255, 0, 0))
        cv2.line(image, (5, row), (640, row), (255, 0, 0), 1)

    for col in range(20, 641, 20):
        cv2.putText(image, col, (col - 5, 5), color=(255, 0, 0))
        cv2.line(image, (col, 5), (col, 480), (255, 0, 0), 1)

    cv2.imshow("image", image)
    rate.sleep()

cv2.destroyAllWindows()