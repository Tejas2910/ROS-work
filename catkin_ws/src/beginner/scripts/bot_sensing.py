#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
count = 0


def read(data):
    theta_min = data.angle_min  # minimum angle in the field of detection
    theta_max = data.angle_max  # maximum angle in the field of detection
    R = data.ranges  # Array containing the distances for different values of angle
    l = len(R)  # length of the array R

    # R[0] corresponds to the distance at theta_min
    # R[l-1] corresponds to the distance at theta_max
    # Intermediate entries correspond to the distances at intermediate angles
    global count
    if count == 0:
        print(R)
        count += 1


if __name__ == "__main__":
    rospy.init_node('bot_sense')
    rospy.Subscriber('/scan', LaserScan, read)
    rospy.spin()
