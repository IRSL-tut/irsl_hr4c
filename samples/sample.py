## jupyter console --kernel=choreonoid
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())
exec(open('/myapps/models/kohaku_robotinterface.py').read())
from irsl_choreonoid_ros.setup_cnoid import SetupCnoid

##
_ri_ = KohakuInterface('/myapps/models/kohaku_robotinterface.yaml')
_robot_ = _ri_.getRobotModel()
SetupCnoid.setEnvironmentFromYaml('package://irsl_sim_environments/cnoid/world/puzzle_blocks.yaml',
                                  setCamera=False, offset=coordinates(fv(0.2,0,0.06)))

##
_robot_.setManipPose()

##
_ri_.sendAngleVector(_robot_.angleVector(), tm=3.0)
_ri_.grasp('right', position=0.6)
_ri_.grasp('left', position=0.6)
_ri_.waitUntilFinish()

#
base_offset_pos = fv(0.2, 0, 0.06)
#
org_cyan_pos   = fv(-0.03, -0.13, 0.016)
org_purple_pos = fv( 0.13,  0.00, 0.046)
org_yellow_pos = fv( 0.13, -0.10, 0.076)
org_red_pos    = fv(-0.06,  0.10, 0.016)
org_lightgreen_pos = fv(0.13,  0.13, 0.016)
org_green_pos  = fv(0.03,  0.185, 0.046)
org_brown_pos  = fv(0.03, -0.20, 0.046)

## _robot_ : robot-model
## _ri_: robot-interface

def approach(org_pos, base_offset_pos=fv(0,0,0), approach_dir=fv(0,0,0.04), arm='right',
             local_offset_pos = None, target_quat=None, tm1=3.0, tm2=1.0, wait=True):

    target_pos = org_pos + base_offset_pos
    if local_offset_pos is not None:
        target_pos += local_offset_pos
    ##
    tgt2 = coordinates(target_pos)
    if target_quat is not None:
        tgt2.quaternion = target_quat
    ##
    tgt1 = tgt2.copy()
    tgt1.translate(approach_dir, coordinates.wrt.world)
    ##
    if arm == 'right' or arm == 'rarm':
        res_, cntr_ = _robot_.rarm.inverseKinematics(tgt2, constraint='xyzRPY')
    else:
        res_, cntr_ = _robot_.larm.inverseKinematics(tgt2, constraint='xyzRPY')
    ##
    ret = False
    if res_:
        v2 = _robot_.angleVector()
        if arm == 'right' or arm == 'rarm':
            res_, cntr_ = _robot_.rarm.inverseKinematics(tgt1, constraint='xyzRPY')
        else:
            res_, cntr_ = _robot_.larm.inverseKinematics(tgt1, constraint='xyzRPY')
        if res_:
            v1 = _robot_.angleVector()
            _ri_.sendAngleVectorSequence( [v1, v2], [tm1, tm2] , wait=True, waitTimeout=15.0)
            ret = True
        else:
            pass
    else:
        pass
    return ret

def _hand_and_move(up_dir, arm='right', tm=1.0, grasp=True, grasp_param=None, wait=True):
    if grasp:
        _ri_.grasp(arm, **grasp_param)
    else:
        _ri_.ungrasp(arm, **grasp_param)
    ##
    if arm == 'right' or arm == 'rarm':
        tgt = _robot_.rarm.endEffector
    else:
        tgt = _robot_.larm.endEffector
    ##
    tgt.translate(up_dir, coordinates.wrt.world)
    if arm == 'right' or arm == 'rarm':
        res_, cntr_ = _robot_.rarm.inverseKinematics(tgt, constraint='xyzRPY')
    else:
        res_, cntr_ = _robot_.larm.inverseKinematics(tgt, constraint='xyzRPY')
    ret = False
    if res_:
        _ri_.sendAngleVector(_robot_.angleVector(), tm, wait=wait, waitTimeout=15.0)
        ret = True
    else:
        pass
    return ret

def pick_up(up_dir, arm='right', tm=1.0, angle=-0.05, wait=True):
    _hand_and_move(up_dir, arm=arm, tm=tm, grasp=True, grasp_param={'position': angle, 'wait': True}, wait=wait)

def place(up_dir, arm='right', tm=1.0, angle=0.6, wait=True):
    _hand_and_move(up_dir, arm=arm, tm=tm, grasp=True, grasp_param={'position': angle, 'wait': True}, wait=wait)

l_o_p=fv(0, 0, 0.012)
app_dir=fv(0, 0, 0.04)

approach(org_cyan_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
pick_up(app_dir, arm='right')
##
approach(org_cyan_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
place(app_dir, arm='right')


approach(org_brown_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
pick_up(app_dir, arm='right')
##
approach(org_brown_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
place(app_dir, arm='right')


approach(org_yellow_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
pick_up(app_dir, arm='right')
##
approach(org_yellow_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='right')
place(app_dir, arm='right')


approach(org_red_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
pick_up(app_dir, arm='left')
##
approach(org_red_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
place(app_dir, arm='left')

_ri_.grasp('left', position=0.9)
approach(org_green_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
pick_up(app_dir, arm='left', angle=0.3)
##
approach(org_green_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
place(app_dir, arm='left', angle=0.9)

approach(org_lightgreen_pos, base_offset_pos=base_offset_pos, target_quat=fv(0, 0, math.sqrt(0.5), math.sqrt(0.5)),
         local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
pick_up(app_dir, arm='left')
##
approach(org_lightgreen_pos, base_offset_pos=base_offset_pos, target_quat=fv(0, 0, math.sqrt(0.5), math.sqrt(0.5)),
         local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
place(app_dir, arm='left')


approach(org_purple_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
pick_up(app_dir, arm='left')
##
approach(org_purple_pos, base_offset_pos=base_offset_pos, local_offset_pos=l_o_p, approach_dir=app_dir, arm='left')
place(app_dir, arm='left')

