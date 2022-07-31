#! /usr/bin/env python

import rospy

# rosmsg type gives output of the form A/B
# The corresponding import statement will be 'from A.msg import B'

from geometry_msgs.msg import Twist


def move():
    rospy.init_node('bot_move', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)

    r = rospy.Rate(10)

    vel_cmd = Twist()

    vel_cmd.linear.x = 0.1  # The bot's heading direction is along the x-axis in its own reference frame
    vel_cmd.angular.z = 0.5

    while not rospy.is_shutdown():
        pub.publish(vel_cmd)
        r.sleep()


if __name__ == '__main__':
    try:
        move()
    except rospy.ROSInterruptException:
        pass
