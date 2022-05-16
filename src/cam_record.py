#!/usr/bin/env python
#-*- coding:utf-8 -*-

import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge


# # https://everyday-image-processing.tistory.com/166

# image = np.array([])
# bridge = CvBridge()

# def img_callback(msg):
#     global image, bridge
#     image = bridge.imgmsg_to_cv2(msg, "bgr8")

# rospy.init_node('cam_record', anonymous=False)
# rospy.Subscriber("/usb_cam/image_raw/", Image, img_callback)

# rate = rospy.Rate(10)
# cnt = 1
# save_frame = True

# out = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 30, (640, 480) )

# while not rospy.is_shutdown():
#     if not image.size == (640 * 480 * 3):
#         continue
    
#     out.write(image)

#     # tf = cv2.imwrite("frame.jpg", image)
#     # print("time: {}".format(time.time()))
#     # print(cnt, tf)
#     cv2.imshow("image", image)
#     # cnt += 1

#     # rospy.sleep(0.5)
#     # rate.sleep()

#     if cv2.waitKey(1) == 27:
#         break
# # out.release()
# # cv2.destroyAllWindows()





def img_callback(data):
    global cv_img
    cv_img = bridge.imgmsg_to_cv2(data, "bgr8")

bridge = CvBridge()
cv_img = np.empty(shape=[0])

rospy.init_node('hough_drive')
rospy.Subscriber("/usb_cam/image_raw", Image, img_callback)
writer= cv2.VideoWriter('/home/lumos/tricat/src/xycar-check/src/output.mp4', cv2.VideoWriter_fourcc(*'DIVX'), 100, (640,480))
cnt = 0
while not rospy.is_shutdown():
    if cv_img.size != (640*480*3):
        continue
    writer.write(cv_img)
    cv2.imshow("cv_img", cv_img)
    if cnt >= 30:
        cv2.imwrite('screenshot{}.png'.format(cnt), cv_img, params=[cv2.IMWRITE_PNG_COMPRESSION,0])
        cnt = 0
    cnt += 1
    cv2.waitKey(1)
    # if cv2.waitKey(1) == 27:
    #     break
    # rospy.sleep(0.2)    