#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def calc(data):
    rospy.loginfo(eval(data.data))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("Input_data", String, calc)
    rospy.spin()

if __name__=='__main__':
        listener()
    
    
