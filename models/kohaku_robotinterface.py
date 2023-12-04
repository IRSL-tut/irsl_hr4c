#### import irsl
#import irsl_choreonoid.robot_util as ru
#import math

from irsl_choreonoid_ros import RobotInterface

class KohakuInterface(RobotInterface):
    def __init__(self, file_name, **kwargs):
        RobotInterface.__init__(self, file_name, **kwargs)

    def graps(self, hand):
        pass

    def ungraps(self, hand):
        pass
