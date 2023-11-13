#### import irsl
import irsl_choreonoid.robot_util
import math

class KohakuModel(irsl_choreonoid.robot_util.RobotModelWrapped):
    def __init__(self, robot):
        super().__init__(robot)
        self.registerEndEffector('larm', ## end-effector
                                 'left_hand_palm_link', ## tip-link
                                 tip_link_to_eef = irsl_choreonoid.robot_util.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
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
                                 tip_link_to_eef = irsl_choreonoid.robot_util.make_coordinates({'pos': [0, 0, 0.07], 'angle-axis': [0, 1, 0, math.pi]}),
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
        self.registerNamedPose('init',
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
        self.setDefaultPose()
    @property
    def lhand(self):
        return self.getLimb('lhand')
    @property
    def rhand(self):
        return self.getLimb('rhand')
