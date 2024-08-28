#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

class CommandHistory:
    def __init__(self):
        self.history = []
        rospy.init_node('command_history_node', anonymous=True)
        rospy.Subscriber('/turtlebot_command', String, self.callback)
        rospy.spin()

    def callback(self, data):
        command = data.data
        self.history.append(command)
        rospy.loginfo(f"Received command: {command}")
        rospy.loginfo(f"Command History: {self.history}")

if __name__ == '__main__':
    try:
        CommandHistory()
    except rospy.ROSInterruptException:
        pass
