Setting up the ROS Drivers for the Robotino
============================================

*Done as from* |last_updated| *. Revert the repository to get the working version that was quoted in the documentation.*

The driver port used is https://github.com/Rahul-K-A/robotino-ros2.git, a ROS2 wrapper for the
Robotino developed by Rahul. Since there are no install instructions, given that you
are setting up his work from a fresh install, there are some dependencies that you have to
fix before the code will build properly in ROS2.

.. code-block:: bash

   cd /path/to/ROS2/src/file
   git clone https://github.com/Rahul-K-A/robotino-ros2.git
   cd ..
   colcon build --symlink-install

.. note::

   The IP Address of the LIDAR is: ``172.27.1.1``, remember to configure it in the computer.

As you may have realised, there will be errors during the building process.
Here are the steps to fix them one by one:

ERROR 1 – Library Dependency Depreciation (Not Fatal, but Recommended)
-----------------------------------------------------------------------

.. code-block:: text

   Starting >>> rto_teleop

   /usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning:
   Usage of dash-separated 'script-dir' will not be supported in future versions.
   Please use the underscore name 'script_dir' instead

   warnings.warn(

   /usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning:
   Usage of dash-separated 'install-scripts' will not be supported in future versions.
   Please use the underscore name 'install_scripts' instead

   warnings.warn(

   ------------------------------------------------------------------------

   Finished <<< rto_teleop [0.72s]

   --- stderr: rto_bringup

   /usr/lib/python3/dist-packages/setuptools/dist.py:723: UserWarning:
   Usage of dash-separated 'script-dir' will not be supported in future versions.
   Please use the underscore name 'script_dir' instead

   warnings.warn(

   ---

   Finished <<< rto_bringup [1.49s]

**FIX:**

- ``cd`` into the ``rto_bringup`` folder within ``src``
- Open ``rto_bringup/setup.cfg``
- Make change to line 2: ``script-dir=$base/lib/rto_bringup`` → ``script_dir=$base/lib/rto_bringup``
- Make change to line 4: ``install-scripts=$base/lib/rto_bringup`` → ``install_scripts=$base/lib/rto_bringup``

ERROR 2 – Missing Dependency Declaration in rto_msgs (FATAL)
------------------------------------------------------------

.. code-block:: text

   --- stderr: rto_msgs

   In file included from /home/robotino/ros_ws/build/rto_msgs/rosidl_generator_c/rto_msgs/msg/detail/north_star_readings__functions.h:19,
   from /home/robotino/ros_ws/build/rto_msgs/rosidl_generator_c/rto_msgs/msg/detail/north_star_readings__functions.c:4:

   /home/robotino/ros_ws/build/rto_msgs/rosidl_generator_c/rto_msgs/msg/detail/north_star_readings__struct.h:24:10:
   fatal error: geometry_msgs/msg/detail/pose__struct.h: No such file or directory

   24 | #include "geometry_msgs/msg/detail/pose__struct.h"
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   compilation terminated.

   gmake[2]: *** [CMakeFiles/rto_msgs__rosidl_generator_c.dir/build.make:457:
   CMakeFiles/rto_msgs__rosidl_generator_c.dir/rosidl_generator_c/rto_msgs/msg/detail/north_star_readings__functions.c.o] Error 1

   gmake[1]: *** [CMakeFiles/Makefile2:213: CMakeFiles/rto_msgs__rosidl_generator_c.dir/all] Error 2
   gmake[1]: *** Waiting for unfinished jobs....

   In file included from /home/robotino/ros_ws/build/rto_msgs/rosidl_typesupport_cpp/rto_msgs/msg/north_star_readings__type_support.cpp:7:

   /home/robotino/ros_ws/build/rto_msgs/rosidl_generator_cpp/rto_msgs/msg/detail/north_star_readings__struct.hpp:22:10:
   fatal error: geometry_msgs/msg/detail/pose__struct.hpp: No such file or directory

   22 | #include "geometry_msgs/msg/detail/pose__struct.hpp"
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   compilation terminated.

   gmake[2]: *** [CMakeFiles/rto_msgs__rosidl_typesupport_cpp.dir/build.make:270:
   CMakeFiles/rto_msgs__rosidl_typesupport_cpp.dir/rosidl_typesupport_cpp/rto_msgs/msg/north_star_readings__type_support.cpp.o] Error 1

   gmake[2]: *** Waiting for unfinished jobs....

   ...

   Failed <<< rto_msgs [4.68s, exited with code 2]

**FIX** – Add back the geometry_msgs dependency in ``CMakeLists.txt``:

- ``cd`` into the ``rto_msgs`` folder within ``src``
- Open ``rto_msgs/CMakeLists.txt``
- Add ``find_package(geometry_msgs REQUIRED)`` underneath ``find_package(ament_lint_auto REQUIRED)``
- Add ``DEPENDENCIES geometry_msgs`` underneath ``DEPENDENCIES builtin_interfaces`` (near the end of the file)

ERROR 3 – Missing Dependency Declaration in rto_node (FATAL)
------------------------------------------------------------

.. code-block:: text

   --- stderr: rto_node

   /home/robotino/ros_ws/src/robotino-ros2/rto_node/src/OdometryROS.cpp:11:10:
   fatal error: tf2_geometry_msgs/tf2_geometry_msgs.h: No such file or directory

   11 | #include "tf2_geometry_msgs/tf2_geometry_msgs.h"
      | ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

   compilation terminated.

   gmake[2]: *** [CMakeFiles/rto_node.dir/build.make:230:
   CMakeFiles/rto_node.dir/src/OdometryROS.cpp.o] Error 1

   gmake[2]: *** Waiting for unfinished jobs....

   gmake[1]: *** [CMakeFiles/Makefile2:141: CMakeFiles/rto_node.dir/all] Error 2

   gmake: *** [Makefile:146: all] Error 2

   ---

   Failed <<< rto_node [6.11s, exited with code 2]

**FIX** – Add back the tf2 dependency in ``CMakeLists.txt``:

- ``cd`` into the ``rto_node`` folder within ``src``
- Open ``rto_node/CMakeLists.txt``
- Add ``find_package(tf2_geometry_msgs REQUIRED)`` underneath ``# find dependencies`` alongside the other dependencies
- Add ``tf2_ros::tf2_ros`` into ``target_link_libraries``:

.. code-block:: cmake

   target_link_libraries(
     rto_node
     ${REC_ROBOTINO_API2_LIBRARY}
     tf2_ros::tf2_ros  # Something like this
   )

- Right under ``target_link_libraries``, add the tf2 library to the dependency list:

.. code-block:: cmake

   ament_target_dependencies(rto_node rclcpp rto_msgs std_msgs geometry_msgs sensor_msgs tf2 tf2_ros tf2_geometry_msgs nav_msgs builtin_interfaces)

That should be all the errors. You may have standard errors (akin to warnings) pop up but
they will be gone the next time you do ``colcon build``. To control with the standard teleop
ros node, remember to remap ``cmd_vel`` to ``/rto3/cmd_vel`` on the robotino (or whatever
your ``cmd_vel`` is called).

.. code-block:: bash

   # To read more on setting up the robotino link to ethernet:
   # https://ip.festo-didactic.com/Infoportal/Robotino3/Hardware/Interfaces/EN/Ethernet.html

   ros2 launch rto_bringup rto_bringup_launch.py hostname:=172.27.1.1

.. code-block:: bash

   ros2 run teleop_twist_keyboard teleop_twist_keyboard --ros-args --remap cmd_vel:=/rto3/cmd_vel

RECOMMENDED FOR ODOMETRY – Adding Odometry Back to the ROS Node
----------------------------------------------------------------

When the Git repository is initially built, the odometry is weirdly not included in the
build files, meaning ROS2 is just unable to output the odometry of the vehicle. To fix
this follow the steps below.

The person maintaining the repository has the odometry node disabled — we need to
re-enable it. Navigate to: ``/src/robotino-ros2/rto_node/src``

**Step 1** – Re-enable the odometry node constructor (``RTOOdometryNode.cpp``):

Change **FROM**:

.. code-block:: cpp

   RTOOdometryNode::RTOOdometryNode():
   Node("rto_odometry_node")
   {
     this->declare_parameter("hostname", "172.26.1.1");
     hostname_ = this->get_parameter("hostname").as_string();
     com_.setName("Odometry");
     initModules();
     timer_ = this->create_wall_timer(200ms, std::bind(&RTOOdometryNode::spin, this))
   }

Change **TO**:

.. code-block:: cpp

   RTOOdometryNode::RTOOdometryNode():
   Node("rto_odometry_node"),
   com_(this)
   {
     this->declare_parameter("hostname", "172.27.1.1");
     hostname_ = this->get_parameter("hostname").as_string();
     com_.setName("Odometry");
     odometry_ = std::make_shared<OdometryROS>(this);
     initModules();
     timer_ = this->create_wall_timer(200ms, std::bind(&RTOOdometryNode::spin, this));
   }

**Step 2** – Update ``initModules()`` to register the odometry with ComROS:

Change **FROM**:

.. code-block:: cpp

   void RTOOdometryNode::initModules()
   {
     com_.setAddress(hostname_.c_str());
     // Set the ComIds
     odometry_.setComId(com_.id());
     com_.connectToServer(false);
   }

Change **TO**:

.. code-block:: cpp

   void RTOOdometryNode::initModules()
   {
     com_.setAddress(hostname_.c_str());
     // Set the ComIds
     odometry_->setComId(com_.id());
     com_.connectToServer(true);
     // Reset my Odometry
     odometry_->set(0, 0, 0);
     // Let ComROS know about the odometry object
     com_.registerOdometry(odometry_.get());
   }

**Step 3** – Add the odometry node to the main launch file at
``/src/robotino-ros2/rto_bringup/launch/rto_bringup_launch.py``:

.. code-block:: python

   Node(
     package='rto_node',
     namespace='rto3',
     executable='rto_odometry_node',
     name='rto_odom',
     parameters=[{'hostname': LaunchConfiguration("hostname")}]
   ),

.. note::

   You can also remove other unused nodes such as the laserscanner to make sure that no
   unexpected nodes are interfering with the ROS network.

With these steps you should now see the odometry node passing data as usual.

Enjoy playing with the Robotino!
