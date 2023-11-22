#!/bin/bash

.irsl_docker/run.sh -w $(pwd) --image irslrepo/irsl_hr4c:noetic --ros-setup /hr4c_ws/devel/setup.bash $@
