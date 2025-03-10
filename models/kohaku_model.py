import os
import math
import irsl_choreonoid.robot_util as ru

class KohakuModel(ru.ImportedRobotModel):
    def __init__(self, robot=None, item=True, world=False, **kwargs):
        super().__init__(robot=robot, item=item, world=world, **kwargs)

    def _init_ending(self, **kwargs): ## override
        self.registerEndEffector('larm', ## end-effector
                                 'left_hand_palm_link', ## tip-link
                                 tip_link_to_eef = ru.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
                                 joint_tuples = (('left_shoulder_yaw',   'shoulder-y'),
                                                 ('left_shoulder_pitch', 'shoulder-p'),
                                                 ('left_elbow_pitch',    'elbow-p'),
                                                 ('left_wrist_yaw',      'wrist-y'),
                                                 ('left_wrist_pitch',    'wrist-p'),
                                                 ('left_hand_yaw',       'hand-y'),
                                                 )
                                 )
        self.registerEndEffector('rarm', ## end-effector
                                 'right_hand_palm_link', ## tip-link
                                 tip_link_to_eef = ru.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
                                 joint_tuples = (('right_shoulder_yaw',   'shoulder-y'),
                                                 ('right_shoulder_pitch', 'shoulder-p'),
                                                 ('right_elbow_pitch',    'elbow-p'),
                                                 ('right_wrist_yaw',      'wrist-y'),
                                                 ('right_wrist_pitch',    'wrist-p'),
                                                 ('right_hand_yaw',       'hand-y'),
                                                 )
                                 )
        self.registerEndEffector('lhand', ## end-effector
                                 'left_l_finger_link', ## tip-link
                                 joint_tuples = (('left_r_finger_joint',   'in-finger'),
                                                 ('left_l_finger_joint',   'out-finger'),
                                                 )
                                 )
        self.registerEndEffector('rhand', ## end-effector
                                 'right_r_finger_link', ## tip-link
                                 joint_tuples = (('right_l_finger_joint',   'in-finger'),
                                                 ('right_r_finger_joint',   'out-finger'),
                                                 )
                                 )
        self.registerNamedPose('initial',
                               [0, 0, 0, 0, 0, 0,  ## larm
                                0, 0,  ## lhand
                                0, 0, 0, 0, 0, 0,  ## rarm
                                0, 0,  ## rhand
                                ])
        self.registerNamedPose('default',
                               [0, math.pi/2, math.pi/2, 0, 0, 0,  ## larm
                                0, 0,  ## lhand
                                0, math.pi/2, math.pi/2, 0, 0, 0,  ## rarm
                                0, 0,  ## rhand
                                ])
        self.registerNamedPose('manip',
                               [ math.pi/6, math.pi/6, 2*math.pi/3, 0, math.pi/6, 0,  ## larm
                                0, 0,  ## lhand
                                -math.pi/6, math.pi/6, 2*math.pi/3, 0, math.pi/6, 0,  ## rarm
                                0, 0,  ## rhand
                               ])
        self.setDefaultPose()

    def setManipPose(self):
        self.setNamedPose('manip')

    @property
    def lhand(self):
        return self.getLimb('lhand')
    @property
    def rhand(self):
        return self.getLimb('rhand')

### settings of model_file
KohakuModel.model_file = f'{os.path.dirname(__file__)}/kohaku_dualarm.body'

### robot_class: 
robot_class = KohakuModel
