#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('Input_data', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    while not rospy.is_shutdown():
        str = raw_input('formula')
        pub.publish(str)

if __name__== '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass

