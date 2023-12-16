#!/bin/bash

#.irsl_docker/run.sh -w $(pwd) --ros-setup /hr4c_ws/devel/setup.bash --image repo.irsl.eiiris.tut.ac.jp/irsl_hr4c:noetic roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false

###
sig_hdl () {
    echo "catch signal $1"
    #if [ -n "$CHILD_PID" ]; then
    #    kill -$1 -${CHILD_PID}
    #fi
    kill -$1 ${LAUNCH_PID}
    exit 0
}
trap "sig_hdl SIGTERM" SIGTERM
trap "sig_hdl SIGINT" SIGINT
trap "sig_hdl SIGHUP" SIGHUP

###

_DISPLAY=":${1:-11}"
_PAUSED=${PAUSED:-true}

LAUNCH_PID=""

export DOCKER_ROS_SETUP=/hr4c_ws/devel/setup.bash
source /irsl_entryrc

gazebo_option=initial_joints:="-J left_shoulder_yaw 0.78539816 -J left_shoulder_pitch 1.3962634 -J left_elbow_pitch 1.74532925 -J right_shoulder_yaw -0.78539816 -J right_shoulder_pitch 1.3962634 -J right_elbow_pitch 1.74532925"
## initial_joints:="-J left_shoulder_pitch 1.57 -J right_shoulder_pitch 1.57 -J left_elbow_pitch 1.57 -J right_elbow_pitch 1.57"


if [ -n "${VGL_DISPLAY}" ]; then
    DISPLAY=$_DISPLAY vglrun roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=${_PAUSED} "${gazebo_option}" &
else
    DISPLAY=$_DISPLAY        roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=${_PAUSED} "${gazebo_option}" &
fi

LAUNCH_PID="$!"

rosrun irsl_sim_environments spawn_puzzle_script.sh

wait ${LAUNCH_PID}

exit 0
