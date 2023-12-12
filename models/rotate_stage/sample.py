rotate_stage_ri=RobotInterface('/myapps/models/rotate_stage/rotate_stage_robotinterface.yaml')

rotate_stage_ri.sendAngleVector([0, 0], tm=2.0) ## flat
rotate_stage_ri.sendAngleVector([-PI/2, 0], tm=2.0) ## up/blue
rotate_stage_ri.sendAngleVector([0, -PI/2], tm=2.0) ## up/yellow
