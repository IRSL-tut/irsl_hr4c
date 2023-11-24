##
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

##
#ri = RobotInterface('/userdir/models/kohaku_robotinterface.yaml')
ri = RobotInterface('/myapps/models/kohaku_robotinterface.yaml', connection=False)
robot = ri.getRobotModel()

##
ri.sendAngleVector(robot.angleVector(), group='wholebody')

##
robot.setDefaultPose()

##
ri.sendAngleVector(robot.angleVector(), tm=5)
ri.waitFinishMoving()

##
robot.larm.endEffector

tgt = robot.larm.endEffector
tgt.translate(npa([0, 0, 0.1]), coordinates.wrt.world)
robot.larm.inverseKinematics(tgt, constraint='xyzRPY')

## hand
robot.lhand.angleVector()
robot.lhand.angleMap
