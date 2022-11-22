import numpy as np
from src.coordinates import Pose
from src.odometry_model import Odometry, OdometryMotionModel as OMM
from src.probability_calculator import ProbabilityUtility as PU

# ODOMETRY
# start = Pose(5.0, 3.0, np.pi / 6)
# end = Pose(8.0, 7.0, 5 * np.pi / 6)
# odometry = OMM.odometry(start, end)

# ODOMETRY MOTION MODEL
# Errors: [RotStart, Trans, RotEnd]
# errors = [0.01, 0.01, 0.01]
# true_odometry = Odometry(0.4, 5.0, 1.69)
# prob = OMM.motion_likelihood(odometry, true_odometry, errors, PU.triangular)
# print(prob)


# SAMPLE FROM DISTRIBUTIONS
# ts = PU.triangular(0.1, 0.5)
# gs = PU.gaussian(0.1, 0.5)