from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    warehouse_pkg_dir = get_package_share_directory('aws_robomaker_small_warehouse_world')
    warehouse_launch_path = os.path.join(warehouse_pkg_dir, 'launch')

    warehouse_world_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([warehouse_launch_path, '/no_roof_small_warehouse.launch.py'])
    )

    # world_file = PathJoinSubstitution(
    #     [FindPackageShare("aws_robomaker_small_warehouse_world"),
    #     "worlds/no_roof_small_warehouse",
    #     "no_roof_small_warehouse.world"],
    # )

    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare("husky_gazebo"),
        "launch",
        "gazebo.launch.py"],
    )

    # The world launch doesn't work when I pass in the world file for some reasons
    # So, I had to disable the gazebo launch inside the husky launch, and instead launch gazebo from aws
    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch]),
        # launch_arguments={'world_path': world_file}.items(),
    )

    ld = LaunchDescription()
    ld.add_action(gazebo_sim)
    ld.add_action(warehouse_world_cmd)
    return ld