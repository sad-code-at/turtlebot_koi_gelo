#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan

class ObstacleIdentifier:
    def __init__(self):
        rospy.init_node('obstacle_identifier', anonymous=True)
        
        # Publisher for obstacle detection
        self.pub = rospy.Publisher('/obstacle', String, queue_size=1)
        
        # Subscriber to the LaserScan topic
        rospy.Subscriber('/scan', LaserScan, self.scan_callback)
        
        self.obstacle_detected = False

    def scan_callback(self, data):
        # Check if any value in the scan ranges is less than or equal to 30 meters
        if any(distance <= 30.0 for distance in data.ranges):
            self.obstacle_detected = True
        else:
            self.obstacle_detected = False

    def run(self):
        rate = rospy.Rate(1)  # 1 Hz
        while not rospy.is_shutdown():
            if self.obstacle_detected:
                rospy.loginfo("Obstacle Found")
                self.pub.publish("Obstacle Found")
            rate.sleep()

if __name__ == '__main__':
    try:
        obstacle_identifier = ObstacleIdentifier()
        obstacle_identifier.run()
    except rospy.ROSInterruptException:
        pass
