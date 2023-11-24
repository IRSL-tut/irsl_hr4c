# Builds

```
cd docker
./build.sh
```

# Run

## Gazebo

```
./run_gazebo.sh
```
## Gazebo with jupyter
```
./exec_jupyter.sh
```

## Gazebo with choreonoid terminal
```
./exec_console.sh
```


## Run (raw command)

### Jupyter Only
```
./run.sh jupyter --ros-setup /hr4c_ws/devel/setup.bash --image repo.irsl.eiiris.tut.ac.jp/irsl_hr4c:noetic
```

### Gazebo
```
./run.sh -w $(pwd) --ros-setup /hr4c_ws/devel/setup.bash --image repo.irsl.eiiris.tut.ac.jp/irsl_hr4c:noetic roslaunch kohaku_launch kohaku_dualarm_bringup.launch sim:=true moveit:=false paused:=false
```

### Gazebo with jupyter
```
./exec.sh -- jupyter lab --allow-root --no-browser --ip=0.0.0.0 --port=8888 --FileCheckpoints.checkpoint_dir=/tmp --ServerApp.token=''
```

### Gazebo with choreonoid terminal
```
./exec.sh -it -- jupyter console --kernel=choreonoid
```
