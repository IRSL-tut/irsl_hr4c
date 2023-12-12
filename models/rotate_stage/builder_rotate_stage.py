# jupyter console --kernel=choreonoid
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())

rb = RobotBuilder()
frame0_color=(0.4, 0.8, 0.8)
frame1_color=(0.8, 0.8, 0.4)
servo_color=(0.3, 0.3, 0.3)
base_color=(0.6, 0.6, 0.6)
## origin

sv0 = rb.makeBox(0.0465, 0.034, 0.0285, color=servo_color)
sv0.translate(fv(-0.012, -0.017, 0))
sv1 = rb.makeBox(0.0465, 0.034, 0.0285, color=servo_color)
sv1.translate(fv(-0.012, -0.017, 0))
cds=coordinates(fv(0, 0.11, 0))
cds.rotate(PI, coordinates.X)
sv1.transform(cds, coordinates.wrt.world)
base = rb.makeBox(0.0465, 0.11 + 0.034*2, 0.008, color=base_color)
base.translate(fv(-0.012, 0.11/2, -(0.0285 + 0.008)/2))
l_root = rb.createLinkFromShape(name='ROOT_FRAME', root=True, density=500.0)

bx0 = rb.makeBox(0.132, 0.11, 0.0205, color=frame0_color)
bx0.translate(fv(0.055, 0.055 ,0))
j0=rb.createJointShape(jointType=Link.JointType.RevoluteJoint)
l0=rb.createLinkFromShape(name='STAGE0', parentLink=l_root, density=500.0, JointId=0, JointName='joint0',
                          JointRange=[-PI, PI], JointVelocityRange=[-PI*10, PI*10], JointEffortRange=[-100, 100], EquivalentRotorInertia=0.05)

bx1 = rb.makeBox(0.132, 0.11, 0.0205, color=frame1_color)
bx1.translate(fv(-0.055, 0.055 ,0))
j1=rb.createJointShape(jointType=Link.JointType.RevoluteJoint)
j1.transform(cds)
l1=rb.createLinkFromShape(name='STAGE1', parentLink=l_root, density=500.0, JointId=1, JointName='joint1',
                          JointRange=[-PI, PI], JointVelocityRange=[-PI*10, PI*10], JointEffortRange=[-100, 100], EquivalentRotorInertia=0.05)

rb.exportBody('/tmp/rotate_stage.body', modelName='rotate_stage')
rb.exportURDF('/tmp/rotate_stage.urdf', RobotName='rotate_stage', UseURDFPrimitiveGeometry=True, UseXacro=False)
