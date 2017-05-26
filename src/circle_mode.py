#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on May 25, 2017 by 9:28 PM

import rospy
from geometry_msgs.msg import Twist


def circle():
    pub = rospy.Publisher('cmd_vel_pub', Twist, queue_size=1)
    rospy.init_node('square_mode')

    cmd_vel = Twist()
    m = rospy.get_param('~diameter', default=2)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        cmd_vel.linear.x = 1.0
        cmd_vel.angular.z = cmd_vel.linear.x/(m/2) #v=w*r
        pub.publish(cmd_vel)

        rospy.loginfo("diameter = {}".format(m))
        rate.sleep()
    # else:
    #     stop = Twist()
    #     pub.publish(stop)
if __name__ == '__main__':
    try:
        circle()
    except rospy.ROSInterruptException:
        pass