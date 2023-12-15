##
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())
exec(open('/myapps/models/kohaku_robotinterface.py').read())
from irsl_choreonoid_ros.setup_cnoid import SetupCnoid

##
ri = KohakuInterface('/myapps/models/kohaku_robotinterface.yaml')
robot = ri.getRobotModel()
SetupCnoid.setEnvironmentFromYaml('package://irsl_sim_environments/cnoid/world/puzzle_blocks.yaml',
                                  setCamera=False, offset=coordinates(fv(0.3,0,0)))

##
robot.setManipPose()

##
ri.sendAngleVector(robot.angleVector(), tm=3.0)
ri.waitFinishMoving()


##
#
##
base_offset_pos = fv(0.2, 0, 0.05)
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
             local_offset_pos = None, target_quat=None, tm1=3.0, tm2=1.0):
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
            _ri_.sendAngleVectorSequence( [v1, v2], [tm1, tm2] )
            ret = True
        else:
            pass
    else:
        pass
    return ret

def _hand_and_move(up_dir, arm='right', tm=1.0, grasp=True, grasp_param=None):
  if grasp:
      _ri_.grasp(arm, **grasp_param)
  else:
      _ri_.ungrasp(arm, **grasp_param)

  if arm == 'right' or arm == 'rarm':
      tgt = _robot_.rarm.endEffector
  else:
      tgt = _robot_.larm.endEffector

  tgt.translate(up_dir, coordinates.wrt.world)
  if arm == 'right' or arm == 'rarm':
      res_, cntr_ = _robot_.rarm.inverseKinematics(tgt, constraint='xyzRPY')
  else:
      res_, cntr_ = _robot_.larm.inverseKinematics(tgt, constraint='xyzRPY')
  ret = False
  if res_:
      _ri_.sendAngleVector(_robot_.angleVector(), tm)
      ret = True
  else:
      pass
  return ret

def pick_up(up_dir, arm='right', tm=1.0):
    _hand_and_move(up_dir, arm=arm, tm=tm, grasp=True, grasp_param={'position': 0.2})

def place(up_dir, arm='right', tm=1.0):
    _hand_and_move(up_dir, arm=arm, tm=tm, grasp=False)
