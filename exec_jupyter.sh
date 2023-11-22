#!/bin/bash

.irsl_docker/exec.sh -- jupyter lab --allow-root --no-browser --ip=0.0.0.0 --port=8888 --FileCheckpoints.checkpoint_dir=/tmp --ServerApp.token=''
