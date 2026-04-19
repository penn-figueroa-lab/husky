from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    hospital_pkg_dir = get_package_share_directory('aws_robomaker_hospital_world')
    hospital_launch_path = os.path.join(hospital_pkg_dir, 'launch')

    hospital_world_cmd = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([hospital_launch_path, '/view_hospital.launch.py'])
    )

    gazebo_launch = PathJoinSubstitution(
        [FindPackageShare("husky_gazebo"),
        "launch",
        "gazebo.launch.py"],
    )

    gazebo_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([gazebo_launch]),
    )

    ld = LaunchDescription()
    ld.add_action(gazebo_sim)
    ld.add_action(hospital_world_cmd)
    return ld