# Robotino ROS2 Documentation

<div align="center">

[![Documentation](https://img.shields.io/badge/docs-online-blue)](https://yeezhen-robotics.github.io/robotino-docs/)
![ROS2](https://img.shields.io/badge/ROS2-Humble-brightgreen)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-orange)
![Built with Sphinx](https://img.shields.io/badge/Built%20with-Sphinx-informational)

📖 **[View the live documentation here](https://yeezhen-robotics.github.io/robotino-docs/)**

</div>

Documentation for the Robotino 3 ROS2 setup. This covers the full software setup of the Robotino 3 platform including ROS2 integration, LIDAR configuration, controller setup, and known build issues encountered during development.

---

## Contents

| Page | Description |
|---|---|
| Robotino Startup Guide | GNU Grub interface, bashrc convenience functions, ROS1/ROS2 sourcing and ros1_bridge workflow |
| ROBOTINO in ROS2 Setup | Build errors and fixes for `robotino-ros2`, odometry re-enabling steps |
| Setting up the LIDAR | Subnet configuration, SOPAS ET setup, and ROS2 launch command for PICS150-01000 Core-1 |
| Setting up the LIDAR Scan Filter | Scan filter workaround using `laser_filters` to avoid the known FOV centering bug |
| Logitech F710 Controller Setup | `joy2twist` install steps, dependency fixes, and dual-dongle bug workaround |
| Writing Launch Files | Guide and references for writing ROS2 launch files |
| SLAM Build Repo Problems | Known issues and fixes for ORBSLAM3, BadSLAM, RE-SLAM, and Ceres-Solver |

---

## System Environment

| | |
|---|---|
| **OS** | Ubuntu 22.04 LTS (Jammy Jellyfish) |
| **ROS Version** | ROS2 Humble |
| **Hardware** | Robotino 3, PICS150-01000 Core-1 LIDAR, Logitech F710 Controller |

---

## Building the Docs Locally

### Prerequisites

```bash
pip install sphinx
```

### Build

```bash
cd Sphinx
.\make.bat html        # Windows
make html              # Linux/Mac
```

The built HTML will be output to `build/html/`. Open `build/html/index.html` in your browser to view locally.

### Clean Build

```bash
.\make.bat clean
.\make.bat html
```

---

## Project Structure

```
Sphinx/
├── source/
│   ├── conf.py                  ← Sphinx configuration
│   ├── index.rst                ← Root table of contents
│   ├── startup_guide.rst
│   ├── robotino_ros2_setup.rst
│   ├── lidar_setup.rst
│   ├── lidar_scan_filter.rst
│   ├── logitech_f710_setup.rst
│   ├── writing_launch_files.rst
│   ├── slam_build_problems.rst
│   ├── _static/
│   │   ├── custom.css           ← Custom styling
│   │   └── images/              ← Robotino and LIDAR images
│   └── _templates/
├── build/
│   └── html/                    ← Generated output (do not edit)
└── docs/                        ← GitHub Pages deployment folder
```

---

## External Repositories Referenced

| Package | Repository |
|---|---|
| robotino-ros2 | [Rahul-K-A/robotino-ros2](https://github.com/Rahul-K-A/robotino-ros2) |
| joy2twist | [husarion/joy2twist](https://github.com/husarion/joy2twist) |
| joystick_drivers | [ros-drivers/joystick_drivers](https://github.com/ros-drivers/joystick_drivers) |
| sick_scan_xd | [SICKAG/sick_scan_xd](https://github.com/SICKAG/sick_scan_xd) |
| ros1_bridge | [ros2/ros1_bridge](https://github.com/ros2/ros1_bridge) |
| ORBSLAM3 | [UZ-SLAMLab/ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3) |
| BadSLAM | [ETH3D/badslam](https://github.com/ETH3D/badslam) |
| RE-SLAM | [fabianschenk/RESLAM](https://github.com/fabianschenk/RESLAM) |
| Ceres-Solver | [ceres-solver/ceres-solver](https://github.com/ceres-solver/ceres-solver) |

---
