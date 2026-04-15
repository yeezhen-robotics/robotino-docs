Installing and Using ros1_bridge
================================

The ``ros1_bridge`` package allows ROS1 and ROS2 nodes to communicate with each other
over the same network. This is useful when some packages are only available in ROS1
(Noetic) and need to interface with ROS2 (Humble) nodes.

- **Repository:** `ros2/ros1_bridge <https://github.com/ros2/ros1_bridge>`_
- **Official Setup Guide:** `ros1_bridge README <https://github.com/ros2/ros1_bridge/blob/master/README.md>`_

.. note::

   The ``ros1_bridge`` must be built from source — it cannot be installed via ``apt``
   as it requires both ROS1 and ROS2 to be present on the same machine at build time.

Building ROS2 and ROS1 packages workflow:

.. code-block:: text

   ros_ws
   |_ src
      |_ ROS1
      |_ ROS2

The workspace is split into two subdirectories so that ROS1 and ROS2 packages can be
built independently without interfering with each other. The build steps must be run
in the correct order — ROS2 first, then ROS1 — and each must be sourced before building.

1. Source Humble

.. code-block:: bash

   source /opt/ros/humble/setup.bash

2. Build only the ROS2 packages:

.. code-block:: bash

   colcon build --symlink-install --packages-ignore-regex src/ROS1

3. Source Noetic:

.. code-block:: bash

   source ~/ros_catkin_ws/install_isolated/setup.bash

4. Build only the ROS1 packages:

.. code-block:: bash

   colcon build --symlink-install --packages-ignore-regex src/ROS2

5. Source both workspaces in two separate terminals, then launch the bridge in a third:

.. code-block:: bash

   # Terminal 1 — source ROS1 and run a ROS1 node
   source ~/ros_catkin_ws/install_isolated/setup.bash
   source ~/ros_ws/install/setup.bash

   # Terminal 2 — source ROS2 and run a ROS2 node
   source /opt/ros/humble/setup.bash
   source ~/ros_ws/install/setup.bash

   # Terminal 3 — launch the bridge
   source /opt/ros/humble/setup.bash
   source ~/ros_catkin_ws/install_isolated/setup.bash
   source ~/ros_ws/install/setup.bash
   ros2 run ros1_bridge dynamic_bridge

.. note::

   The ``dynamic_bridge`` automatically creates bridges for any topics that have
   matching publishers and subscribers on both sides. If you only need to bridge
   specific topics, use ``parameter_bridge`` instead for better performance.