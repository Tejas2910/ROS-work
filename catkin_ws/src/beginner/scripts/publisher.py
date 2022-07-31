#!/usr/bin/env python
import rospy
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('listen1', String, queue_size=10)
    rospy.init_node('publisher1', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "world"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
