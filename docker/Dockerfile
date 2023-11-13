ARG BASE_IMAGE=repo.irsl.eiiris.tut.ac.jp/irsl_system:noetic

FROM ${BASE_IMAGE}

LABEL maintainer "IRSL-tut (https://github.com/IRSL-tut) <faculty@irsl.eiiris.tut.ac.jp>"

SHELL ["/bin/bash", "-c"]

WORKDIR /hr4c_ws

RUN source /opt/ros/${ROS_DISTRO}/setup.bash && \
    wstool init src && \
    wstool set hr4c_common_pkgs        https://github.com/QibiTechInc/hr4c_common_pkgs.git         -y -t src --git && \
    wstool set kohaku_ros_pkgs         https://github.com/QibiTechInc/kohaku_ros_pkgs.git          -y -t src --git && \
    wstool set kohaku_ros_examples     https://github.com/QibiTechInc/kohaku_ros_examples.git      -y -t src --git && \
    wstool set realsense_gazebo_plugin https://github.com/pal-robotics/realsense_gazebo_plugin.git -y -t src --git && \
    wstool set realsense_ros           https://github.com/IntelRealSense/realsense-ros.git         -y -t src --git -v ros1-legacy && \
    wstool update -t src

RUN apt update -q -qq && \
    rosdep update -y -q -r && \
    rosdep install -y -q -r --ignore-src --from-path src && \
    apt clean && \
    rm -rf /var/lib/apt/lists/
    
RUN source /choreonoid_ws/install/setup.bash && catkin build

## COPY 