#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created by Chukwunyere Igbokwe on May 25, 2017 by 9:28 PM

import rospy
from geometry_msgs.msg import Twist
import numpy as np


class SquareMode():
    def __init__(self):
        rospy.init_node('square_mode')
        self.pub = rospy.Publisher('cmd_vel_pub', Twist, queue_size=1)
        self.twist = Twist()
        self.rate = rospy.Rate(10)
        self.linear_speed = 1.0
        self.length = rospy.get_param('~length', default=2)
        self.desired_angle = np.pi/2


    def _staight(self):
        self.twist.linear.x = self.linear_speed
        self.twist.angular.z = 0
        current_distance = 0
        t0 = rospy.Time.now().to_sec()
        while (current_distance < self.length):
            self.pub.publish(self.twist)
            t1 = rospy.Time.now().to_sec()
            current_distance = self.linear_speed * (t1 - t0)
            rospy.loginfo("Moving. Distance = {}".format(current_distance))
            self.rate.sleep()
            # Force the robot to stop once the goal is reached
        self.twist.linear.x = 0
        self.pub.publish(self.twist)
        rospy.sleep(0.5)


    def _rotate(self):
        self.twist.linear.x = 0
        self.twist.angular.z = np.pi/2
        current_angle = 0
        t0 = rospy.Time.now().to_sec()
        while (abs(current_angle) < abs(self.desired_angle)):
            self.pub.publish(self.twist)
            t1 = rospy.Time.now().to_sec()
            current_angle = np.pi/2* (t1 - t0)
            rospy.loginfo("Rotating. {} degrees".format(current_angle * 180/np.pi))
            self.rate.sleep()

            # Force the robot to stop once the orientation is reached
        self.twist.angular.z = 0
        self.pub.publish(self.twist)
        rospy.sleep(0.5)

    def square(self):

        while True:
            self._staight()
            self._rotate()


if __name__ == '__main__':
    try:
        sq = SquareMode()
        sq.square()
    except rospy.ROSInterruptException:
        pass


