#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

# # https://everyday-image-processing.tistory.com/166

def img_callback(data):
    global cv_img
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")

bridge = CvBridge()
cv_img = np.empty(shape=[0])

rospy.init_node('hough_drive')
rospy.Subscriber("/usb_cam/image_raw", Image, img_callback)
writer= cv2.VideoWriter('/home/lumos/tricat/src/xycar-check/src/output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 100, (640,480))
cnt = 0
img_num = 1
while not rospy.is_shutdown():
    if cv_img.size != (640*480*3):
        continue
    
    writer.write(cv_img)
    
    cv2.imshow("cv_img", cv_img)

    if cnt >= 100:
        cv2.imwrite('video_{}.jpg'.format(img_num), cv_img, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
        cnt = 0
    cnt += 1

    cv2.waitKey(1)

    # if cv2.waitKey(1) == 27:
    #     break
    # rospy.sleep(0.2)    