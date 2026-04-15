Setting up the LIDAR's Scan Filter (PICS150-01000 Core-1)
=========================================================

.. warning::

   **DO NOT THRESHOLD THE FIELD OF VIEW OF THE LIDAR IN THE DRIVER.** There is a known issue
   whereby the driver incorrectly breaks the centering of the field of view if the range is
   thresholded in the code. This includes changing the parameter in the launch files. Instead,
   do what is suggested below.

.. code-block:: bash

   mkdir launch  # Make launch directory in the ros workspace
   # In the launch directory, create two files: scan_filter.yaml and scan_filter_launch.py

In ``scan_filter.yaml``:

.. code-block:: yaml

   scan_to_scan_filter_chain:
     ros__parameters:
       filter1:
         name: angle_filter
         type: laser_filters/LaserScanAngularBoundsFilter
         params:
           lower_angle: -1.221
           upper_angle: 1.221

In ``scan_filter_launch.py``:

.. code-block:: python

   import os
   from launch import LaunchDescription
   from launch_ros.actions import Node

   def generate_launch_description():
     with open('/home/robotino/ros_ws/launch/scan_filter.yaml', 'r') as f:
       filter_chain = f.read()

     return LaunchDescription([
       Node(
         package='laser_filters',
         executable='scan_to_scan_filter_chain',
         name='scan_to_scan_filter_chain',  # must match the YAML top-level key
         parameters=['/home/robotino/ros_ws/launch/scan_filter.yaml'],
         remappings=[
           ('scan', '/scan'),
           ('scan_filtered', '/scan_filtered'),
         ],
       ),
     ])

In terminal, run:

.. code-block:: bash

   ros2 launch launch/scan_filter_launch.py
