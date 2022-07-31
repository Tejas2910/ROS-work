#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
msg = ""

def callback1(data):
    global msg
    msg = data.data
    print(msg)

def listener():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber("chatter", String, callback1)
    rospy.spin()


if __name__ == '__main__':
    listener()
