from coordinates import Point, Pose
from differential_drive import DifferentialDrive
from odometry_model import Odometry, OdometryMotionModel
from probability_calculator import ProbabilityUtility, MarginalSpace, State
from scan_sensor_model import ScanSensorModel
import numpy as np


ssm = ScanSensorModel()

sensors = ssm.get_rel_sensor_poses(0.5, np.pi/3)
interest_sensor = sensors[1]
pose = ssm.get_abs_sensor_pose(Pose(7, 4, np.pi/2), interest_sensor)

print(pose)
