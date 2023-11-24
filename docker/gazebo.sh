#!/bin/bash

#.irsl_docker/run.sh -w $(pwd) --ros-setup /hr4c_ws/devel/setup.bash --image repo.irsl.eiiris.tut.ac.jp/irsl_hr4c:noetic roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false

_DISPLAY=":${1:-11}"

export DOCKER_ROS_SETUP=/hr4c_ws/devel/setup.bash
source /irsl_entryrc

if [ -n "${VGL_DISPLAY}" ]; then
    DISPLAY=$_DISPLAY vglrun roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false
else
    DISPLAY=$_DISPLAY roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false
fi
