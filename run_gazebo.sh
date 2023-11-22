#!/bin/bash

.irsl_docker/run.sh -w $(pwd) --ros-setup /hr4c_ws/devel/setup.bash --image repo.irsl.eiiris.tut.ac.jp/irsl_hr4c:noetic roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false
