#!/bin/bash

BASE_IMG=irslrepo/irsl_system:noetic

docker build .. --progress=plain --pull -f Dockerfile \
       --build-arg BASE_IMAGE=${BASE_IMG} -t irslrepo/irsl_hr4c:noetic

## docker login
## docker push irslrepo/irsl_hr4c:noetic
