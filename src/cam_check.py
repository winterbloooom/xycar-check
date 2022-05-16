#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

image = np.array([])
bridge = CvBridge()

def img_callback(msg):
    global image, bridge
    image = bridge.imgmsg_to_cv2(msg, "bgr8")

rospy.init_node('cam_test', anonymous=False)
rospy.Subscriber("/usb_cam/image_raw/", Image, img_callback)

rate = rospy.Rate(10)

font =  cv2.FONT_HERSHEY_SIMPLEX

while cv2.waitKey(1) != 27: #not rospy.is_shutdown():
    while not image.size == (640 * 480 * 3):
        continue

    for row in range(50, 481, 50):
        # TODO 글자 위치 조정
        cv2.putText(image, str(row), (2, row + 3), font, 0.3, (200, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(row), (615, row + 3), font, 0.3, (200, 0, 0), 1, cv2.LINE_AA)
        cv2.line(image, (25, row), (610, row), (255, 0, 0), 1)

    for col in range(50, 641, 50):
        cv2.putText(image, str(col), (col - 10, 10), font, 0.3, (200, 0, 0), 1, cv2.LINE_AA)
        cv2.putText(image, str(col), (col - 10, 473), font, 0.3, (200, 0, 0), 1, cv2.LINE_AA)
        cv2.line(image, (col, 15), (col, 465), (255, 0, 0), 1)

    cv2.imshow("image", image)
    rate.sleep()

cv2.destroyAllWindows()