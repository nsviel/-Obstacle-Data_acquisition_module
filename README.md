# [Obstacle] Data Acquisition Module

This module is in charge of receiving the LiDAR output data, transmiting it to an Edge server and assuring inter-communication between up-level module and the LiDAR in order to remotly command the LiDAR parameters (e.g, motor activation, speed).
 
![capture](https://user-images.githubusercontent.com/80487132/220365897-bfaf5de9-b103-4b8c-b224-64be1a14131a.png)

## Installation and execution

<details><summary>Installation</summary>

Simply run the script file
```
./install.sh
```
In the program directory.

</details>
<details><summary>Execution</summary>

Simply run by the command
```
./run.sh
```

</details>
<details><summary>Docker</summary>

You can use a docker image with:

```
cd docker
./build.sh
./run.sh
```

</details>

## Documentation

<details><summary>General</summary>

- The more important parameters could be changed in the ```config``` JSON file.

</details>

<details><summary>Links</summary>

Full system repository: [link](https://github.com/nsviel/Obstacle_System)<br />
- [x] Data acquisition module
- [ ] Control Interface module: [link](https://github.com/nsviel/Obstacle-Control_Interface_Module)
- [ ] Edge server module
  - [ ] Edge orchestrator component: [link](https://github.com/nsviel/Obstacle-Edge_Orchestration_Module)
  - [ ] Data processing component: [link](https://github.com/nsviel/Velodium)

</details>
