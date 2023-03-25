# Quadrotor Simulator Workspace

This codebase contains the implementation for a quadrotor simulator.

## Overview
This repository is a `colcon` workspace. You can learn more about
`colcon` [here](https://colcon.readthedocs.io/en/released/).

The `wet` folder contains git submodules under active development.
1. `quadrotor_simulator_py`: Python codebase with C++ bindings

The `dry` folder contains git submodules for third party dependencies.
1.

## Quick Start
### Machines
This codebase has been tested on:

1. MacBook Pro (16-inch, 2019): 2.4 GHz 8-Core Intel Core i9 processor, 64 GB 2667 MHz DDR4 RAM, MacOS Catalina v10.15.7.

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
pip install numpy cprint
```

## Build and Install
We depend on a specific version of `Eigen`. For convenience, a
separate `colcon` workspace is provided that can be utilized as
follows:
```
cd dry
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
cd ..
source workon
```
You will observe that `eigen_colcon` is built.

Now we switch back to `wet` and compile our target codebase.
```
cd wet
colcon build --symlink-install --cmake-args -DCMAKE_BUILD_TYPE=Release
cd ..
source workon
```
You should now be ready to use our API in `ipython` or run the scripts provided
in `quadrotor_simulator_py` submodule.

Several tutorials and API details are provided in the documentation as detailed next.

### Quick Test (Quadrotor Model, Dynamics, and Control)

```
cd wet/src/quadrotor_simulator_py/unittest
curl -L https://cmu.box.com/shared/static/tby767h8vzzbwo45bo76i1t9qjf144kw.bag --output data/rocky0704_minimal.bag
python TestQuadrotorModel.py
```

The output should look like the following:

TODO

## Documentation
We provide documentation at three levels:
TODO

Instructions to compile the documentation locally are as follows.

## Authors
Wennie Tabib, Kshitij Goel
