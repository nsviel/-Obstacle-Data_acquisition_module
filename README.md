# [Obstacle] Data Acquisition Module

This module is in charge of receiving the LiDAR output data, transmiting it to an Edge server and assuring inter-communication between up-level modules and the LiDAR in order to remotly command the LiDAR parameters (e.g, motor activation, speed).

![capture](https://user-images.githubusercontent.com/80487132/220365897-bfaf5de9-b103-4b8c-b224-64be1a14131a.png)

## Documentation
<details><summary>Installation and execution</summary>

To install dependencies, simply run the script file
```
./install.sh
```
in the program directory.
Start the program by the command
```
./run.sh
```
:warning: root privileges are required

</details>
<details><summary>Docker</summary>

You can use a docker image with:

```
cd docker
./build.sh
./run.sh
```

</details>

<details><summary>Configuration</summary>

The more important parameters could be changed in the ```config``` JSON file.

</details>

## System

Full system repository ( [link](https://github.com/nsviel/Obstacle_detection_system) )
- [x] Data acquisition module
- [ ] Edge server module
  - [ ] Edge orchestrator component ( [link](https://github.com/nsviel/-Obstacle-Edge_orchestrator_component) )
  - [ ] Data processing component ( [link](https://github.com/nsviel/-Obstacle-Data_processing_component) )
  - [ ] AI component
- [ ] Control Interface module ( [link](https://github.com/nsviel/-Obstacle-Control_interface_module) )
