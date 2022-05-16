#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import cv2
from xycar_msgs.msg import xycar_motor

rospy.init_node('motor_test', anonymous=False)
pub = rospy.Publisher('xycar_motor', xycar_motor, queue_size=1)
rate = rospy.Rate(10)
motor = xycar_motor()

cv2.namedWindow("trackbar")
cv2.createTrackbar('speed','trackbar', 0, 30, lambda x : x)
cv2.createTrackbar('angle','trackbar', 0, 100, lambda x : x)

while cv2.waitKey(1) != 27: #not rospy.is_shutdown():
    motor.speed = cv2.getTrackbarPos('speed', 'trackbar') #3
    motor.angle = cv2.getTrackbarPos('angle', 'trackbar') #0
    print("speed : {} / angle : {}".format(motor.speed, motor.angle))
    pub.publish(motor)
    rate.sleep()

cv2.destroyAllWindows()