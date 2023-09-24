# def main():
#     print('Hi from state.')


# if __name__ == '__main__':
#     main()


import rclpy
from rclpy.node import Node
import smach


rclpy.init()
_node = Node('state_machine2')


class FOo(smatch.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1','outcome2'])
        self.counter = 0
        self.logger = _node.get_logger()

    def execute(self, userdata):
        self.logger.info('implement state F00')
        if self.counter < 3:
            self.counter +1
            return 'outcome1'
        else:
            return 'outcome2'


class Bar(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['outcome1'])
        self.logger = _node.get_logger()

    def execute(self.userdata):
        self.logger.info("implement state BAR")


def main():
    sm = smach.StateMachine(outcomes=['outcome4'])