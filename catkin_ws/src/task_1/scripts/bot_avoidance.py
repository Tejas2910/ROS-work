#! /usr/bin/env python

import rospy
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist

def clbk_laser(data):
	regions = {
		'right':  data.ranges[-180],
		'front':  data.ranges[0],
		'left':   data.ranges[180]}
    
	vel = Twist()
	linear_x = 0
	angular_z = 0
	d = 0.7
	
	if regions['front'] > d:
		linear_x = 0.5
		angular_z = 0
	elif regions['front'] < d and regions['right'] > 0.20:
		linear_x = 0
		angular_z = -0.25
	else:
		linear_x = 0
		angular_z = 0.25  
		
	vel.linear.x = linear_x
	vel.angular.z = angular_z
	pub.publish(vel)


if __name__ == '__main__':
    rospy.init_node('bot_avoidance', anonymous = True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    sub = rospy.Subscriber('/scan', LaserScan, clbk_laser)
    rospy.spin()
    
    