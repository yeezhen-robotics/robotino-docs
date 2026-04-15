Logitech F710 Controller to Robotino in ROS2 Important Setup Steps
===================================================================

*Done as from* |last_updated| *. Revert the repository to get the working version that was quoted in the documentation.*

We will be running https://github.com/husarion/joy2twist, a ROS2 controller for the Logitech
F710 developed by husarion. The node allows the controller to send ``cmd_vel`` messages to
the Robotino. Since the install instructions are vague, there are some dependencies that you
have to fix before the code will build properly in ROS2.

.. code-block:: bash

   # Install important external repositories/dependencies for the controller.
   sudo apt update
   sudo apt install libspnav-dev
   sudo apt install libbluetooth-dev
   sudo apt install libcwiid-dev
   sudo apt install joystick

   cd YOUR_ROS2_WORKSPACE
   source $YOUR_ROS2_INSTALLATION

   cd src  # Head into source directory
   git clone https://github.com/husarion/joy2twist.git
   git clone https://github.com/ros-drivers/joystick_drivers.git
   cd ..  # Return to higher directory

   # REALLY IMPORTANT: joy is a CORE PACKAGE and the command below will overwrite it.
   # This comment is written so you are aware (if another repo uses the joystick it may break something)
   colcon build --symlink-install --allow-overriding joy

   # Test if your controller is working (If you have multiple dongles, try all the ports)
   jstest /dev/input/js0

BUG: Mouse Issue When Having Two Dongles Plugged In at Once
-----------------------------------------------------------

This only applies if you have a mouse and a Logitech dongle plugged into two different ports of the PC.
Always, ALWAYS plug in the mouse dongle first, doing it before startup.
There is a weird data transferring issue going on if the Logitech controller is plugged in first.

.. code-block:: bash

   ls /dev/input/js*  # Lists all input USBs

   # Check which port corresponds to which device
   jstest /dev/input/js1
   jstest /dev/input/js0  # etc

   # Make sure the mouse dongle is js0, if not restart the PC
