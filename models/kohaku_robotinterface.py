#### import irsl
#import irsl_choreonoid.robot_util as ru
#import math

from irsl_choreonoid_ros import RobotInterface

class KohakuInterface(RobotInterface.RobotInterface):
    def __init__(self, file_name, **kwargs):
        RobotInterface.RobotInterface.__init__(self, file_name, **kwargs)

        if not self.connected:
            self.is_real_robot = False
            return

        self.is_real_robot = self.isRealRobot()

        if self.is_real_robot:
            self.right_gripper_action = RobotInterface.GripperInterface('/kohaku_righthand/gripper_cmd')
            self.left_gripper_action  = RobotInterface.GripperInterface('/kohaku_lefthand/gripper_cmd')

    def grasp(self, hand, position, effort=10):
        hh = hand.lower()
        if hh == 'l' or hh == 'left':
            hand = 'left'
        else:
            hand = 'right'

        if self.is_real_robot:
            pass
        else:
            jg = self.getJointGroup('{}hand'.format(hand))
            jg.sendAnglesSequence(((position, position), ), (effort/10.0, ))

    def ungrasp(self, hand, effort=10):
        if self.is_real_robot:
            pass
        else:
            self.grasp(hand, 1.5708, effort)
