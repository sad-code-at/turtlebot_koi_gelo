#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from nav_msgs.msg import Odometry

class PositionTurtle:
    def __init__(self):
        rospy.init_node('position_turtle', anonymous=True)
        
        # Publisher for turtle position
        self.pub = rospy.Publisher('/turtle_pos_xy', String, queue_size=1)
        
        # Subscriber to the odometry topic
        rospy.Subscriber('/odom', Odometry, self.odom_callback)
        
        self.position = None
        self.rate = rospy.Rate(0.2)  # 5 seconds

    def odom_callback(self, data):
        # Extract the current position of the TurtleBot
        self.position = data.pose.pose.position

    def run(self):
        while not rospy.is_shutdown():
            if self.position:
                pos_str = f"Current Position: x={self.position.x:.2f}, y={self.position.y:.2f}"
                rospy.loginfo(pos_str)
                self.pub.publish(pos_str)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        position_turtle = PositionTurtle()
        position_turtle.run()
    except rospy.ROSInterruptException:
        pass
