import numpy as np
from src.coordinates import Pose, Point
from src.scan_sensor_model import ScanSensorModel as SSM
from src.probability_calculator import ProbabilityUtility as PU

# # SENSOR LOCATION BASED ON POSE AND ANGLES
# rotangle = np.pi / 3
# radius = 0.5
# pose = Pose(7, 4 , np.pi/2)

# sensor_relative_poses = SSM.get_rel_sensor_poses(radius, rotangle)
# sensor_global_poses = [SSM.get_abs_sensor_pose(pose, sensor_relative_pose) for sensor_relative_pose in sensor_relative_poses]
# print(sensor_global_poses[1])


# # READING LIKELIHOOD
# real_landmark_point = Point(8.0, 6.0)
# measured_landmark_point = Point(3.0, 4.0)
# measured_distance = 5
# std = np.sqrt(0.3)
# reading_likelihood = SSM.get_reading_likelihood(real_landmark_point, measured_landmark_point, measured_distance, std, PU.triangular)
# print(reading_likelihood)


# SCAN LOCATION
# local_sensor_pose = Pose(0.0, 0.0, np.pi)

# robot_pose = Pose(0.0, 0.0, np.pi)
# scan_distance = 10
# global_sensor_pose = SSM.get_abs_sensor_pose(robot_pose, local_sensor_pose)
# SSM.get_reading_location(global_sensor_pose, scan_distance)