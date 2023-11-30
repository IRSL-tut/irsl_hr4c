#!/bin/bash

_DISPLAY=":${1:-11}"

export DOCKER_ROS_SETUP=/hr4c_ws/devel/setup.bash
source /irsl_entryrc

rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/red_block/red_block.urdf -model red_block -x 0.3 -y 0.1 -z 0.1
rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/blue_block/blue_block.urdf -model blue_block -x 0.3 -y -0.1 -z 0.1
rosrun gazebo_ros spawn_model -urdf -file $(rospack find irsl_sim_environments)/urdf/puzzle_blocks/puzzle_base.urdf -model puzzle_base -x 0.32 -z 0.04
