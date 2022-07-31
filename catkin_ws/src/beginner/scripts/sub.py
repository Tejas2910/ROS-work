#!/usr/bin/env python
import rospy
from std_msgs.msg import String
data1 = ""


def callback0(data):
    global data1
    data1= str(data.data)
    
def callback1(data):
    global data1
    data2 =  str(data.data) + " " + data1
    print(data2)

    
if __name__ == '__main__':
    #initialize the subscriber node called 'listener'
    rospy.init_node('listener', anonymous=True)
    #This is to subscribe to the messages from the topic named 'chatter'
    rospy.Subscriber("listen2", String, callback1)
    rospy.Subscriber("listen1", String, callback0)
    #rospy.loginfo(l.data1 + " "  + l.data2)  
    #print(l.data1)
    # spin() simply keeps python from exiting until this node is stopped

    rospy.spin()