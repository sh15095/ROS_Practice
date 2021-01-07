import rospy
import actionlib

from my_robot_msgs.msg import CountUntilAction, CountUntilGoal

class CountUntilClient:
    def __init__(self):
        self._ac = actionlib.SimpleActionClient('/count_until', CountUntilAction)
        self._ac.wait_for_server()
        rospy.loginfo('Simple Action Client is ready to interact with the server')

    def send_goal_get_result(self):
        goal = CountUntilGoal(count_untill = 3, wait_untill=0.9)
        self._ac.send_goal(goal)
        rospy.loginfo('Goal has been sent')
        self._ac.wait_for_result(rospy.Duration(3.0))
        rospy.loginfo(self._ac.get_result())

if __name__=='__main__':
    rospy.init_node('count_until_action')

    client = CountUntilClient()

    client.send_goal_get_result()
    
