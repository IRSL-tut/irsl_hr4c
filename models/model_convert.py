# jupyter console --kernel=choreonoid
exec(open('/choreonoid_ws/install/share/irsl_choreonoid/sample/irsl_import.py').read())
rb = iu.loadRobot('models/kohaku.urdf')
lk=rb.link('camera_link')
lk.visualShape.getChild(0).setUri('resource/camera_mesh.scen', 'resource/camera_mesh.scen')
iu.exportBody('models/kohaku_dualarm.body', rb, extModelFileMode=2, fixMassParam=True)
#iu.exportBody('models/kohaku_dualarm.body', rb, extModelFileMode=2)
#for ll in rb.links:
#   mass = ll.mass
#   II = ll.I
#   if mass == 1.0 and II[0][0] == 1.0 and II[1][1] == 1.0 and II[2][2] == 1.0 and II[0][1] == 0.0 and II[0][2] == 0.0 and II[1][2] == 0.0:
#       print('link: {}, small mass-paramters is set'.format(ll.name))
#       ll.setMass(0.001)
#       ll.setInertia( npa( ((1.0, 0, 0), (0, 1.0, 0), (0, 0, 1.0)) ) * 1e-9 )
