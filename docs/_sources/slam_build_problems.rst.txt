Misc: SLAM Build Repo Problems
==============================

This section documents any issues encountered while installing SLAM repositories.

ORBSLAM3
--------

| **Repository:** `UZ-SLAMLab/ORB_SLAM3 <https://github.com/UZ-SLAMLab/ORB_SLAM3>`_
| ORB-SLAM3: An Accurate Open-Source Library for Visual, Visual-Inertial and Multi-Map SLAM

This is the only SLAM repository I was able to get working as an example. Remember to add Pangolin and RealsenseViewer to path.

.. code-block:: bash

   export PATH="$PATH:~/Dependency_WS/Pangolin/build"
   export PATH="$PATH:/opt/ros/humble/lib/x86_64-linux-gnu"

BadSLAM
-------

| **Repository:** `ETH3D/badslam <https://github.com/ETH3D/badslam>`_
| Bundle Adjusted Direct RGB-D SLAM

Builds with no issue, but unfortunately requires CUDA.

RE-SLAM
-------

| **Repository:** `fabianschenk/RESLAM <https://github.com/fabianschenk/RESLAM>`_
| RESLAM: A real-time robust edge-based SLAM system

Source Pangolin and Ceres-Solver. Does not work due to dependency conflicts across different Python versions.

.. code-block:: bash

   export PATH="$PATH:~/Dependency_WS/Pangolin/build"

Ceres-Solver
------------

| **Repository:** `ceres-solver/ceres-solver <https://github.com/ceres-solver/ceres-solver>`_
| A large scale non-linear optimization library

Ignore glog (Dependency Clash — will just remove logging capabilities):

.. code-block:: bash

   cmake .. -DMINIGLOG=ON
