# Quadrotor Simulator Workspace

This codebase contains the implementation for a quadrotor simulator.

## Overview
This repository is a `colcon` workspace. You can learn more about
`colcon` [here](https://colcon.readthedocs.io/en/released/).

The `wet` folder contains git submodules under active development.
1. `quadrotor_simulator_py`: Python codebase with C++ bindings
2. `quadrotor_simulator_ros`: ROS2 interface for `quadrotor_simulator_py` (only for Ubuntu)

The `dry` folder contains git submodules for third party dependencies.
1. `eigen_colcon`: A getter for the Eigen library

## Quick Start

### Pre-requisites
#### Compile-Time Dependencies
We require using a Python 3.8 virtual environment using `pip`. Assume that the
virtual environment is created within this repository using the folder name
`.venv`. First we set up the `colcon` build environment.

```
git clone git@github.com:rislab/quadrotor_simulator_ws.git --recursive
cd quadrotor_simulator_ws
python3.8 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install colcon-common-extensions
```

#### Run-Time Dependencies
For python scripts, run-time dependencies can be installed using `pip`. Make sure
the virtual environment created above is active.
```
pip install numpy cprint scipy progressbar matplotlib rosbags future
```

## Build and Install
To build, simply run:

```bash
./build
```

To use the codebase, run:

```bash
source workon
```

## Data Download
Download data
```python
source .venv/bin/activate
cd data
pip install gdown
python download.py
```

## Run Simulation Stack
```python
cd wet/src/quadrotor_simulator_py/unittest
```
Then run the tests in the following packages.

### Test Quadrotor Model
```python
python TestQuadrotorModel.py
```

### Test Position Controller
```python
python TestPositionControllerPD.py
```

### Test Attitude Controller
```python
python TestAttitudeControllerPD.py
```

### Test Quadrotor Dynamics and Control
```python
python TestQuadrotorDynamicsControl.py
```

### Visualization via ROS2
Follow installation for ROS2 here: https://docs.ros.org/en/foxy/Installation.html

```bash
ros2 launch quadrotor_simulator_ros main.xml
```

## Authors
Wennie Tabib, Kshitij Goel
