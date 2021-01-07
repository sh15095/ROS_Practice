import rospy 
import actionlib
from my_robot_msgs.msg import CountUntilAction, CountUntilGoal, CountUntilResult

class CountUntilServer:
    def __init__(self):
        self._as = actionlib.SimpleActionServer('/count_until',
                CountUntilAction,execute_cb=self.on_goal,auto_start=False)
        self._as.start()
        self._counter=0
        rospy.loginfo('Simple Action Server has started')
    def on_goal(self, goal):
        rospy.loginfo('It has received the goal')
        rospy.loginfo(goal)

        count_until = goal.count_untill
        wait_until = goal.wait_untill
        self._counter = 0

        rate = rospy.Rate(1/wait_until)

        while self._counter < count_until:
            self._counter += 1
            rospy.loginfo(self._counter)
            rate.sleep()
        
        result = CountUntilResult()
        result.counted_untill = self._counter

        self._as.set_succeeded(result)


if __name__ == '__main__':
    rospy.init_node('count_until_server')

    server = CountUntilServer()

    rospy.spin()


