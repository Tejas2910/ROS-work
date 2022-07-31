#!/usr/bin/env python
  
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge, CvBridgeError


def callback(img_msg):
    # Initialize the CvBridge class
    bridge = CvBridge()
    # Print some info of image to the Terminal and to a ROS Log file located in ~/.ros/log/loghash/*.log
    rospy.loginfo(img_msg.header)

    # Try to convert the ROS Image message to a CV2 Image
    try:
        cv_image = bridge.imgmsg_to_cv2(img_msg, "passthrough")
    except CvBridgeError as e:
        rospy.logerr("CvBridge Error: {0}".format(e))

    # Convert the image to Grayscale
    gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
    # Show the converted image
    cv2.namedWindow("Image Window", 1)
    cv2.imshow("Image Window", gray)
    cv2.waitKey(3)


def laser():
    rospy.Subscriber('/camera/rgb/image_raw', Image, callback)
    rospy.spin()


if __name__ == '__main__':
    rospy.init_node('cvbridge_example', anonymous=True)
    try:
        laser()

    except rospy.ROSInterruptException:
        pass