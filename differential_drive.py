import numpy as np
from src.coordinates import *
from src.differential_drive import DifferentialDrive as DD
from src.probability_calculator import ProbabilityUtility as PU

# PARAMETERS
# w = np.pi
# v = np.pi
# vr = np.pi * 3
# vl = np.pi * 2
# pose = Pose(0.0, 0.0, np.pi)
# l = 4
# icrrad = np.pi

# BASIC DIFFERENTIAL DRIVE
# icrrad = DD.icr_radius_given_velocity_and_angular(v, w)
# icrrad = DD.icr_radius_given_wheel_velocities(vr, vl, l)
# icrrad = DD.icr_given_pose_and_icr_radius(pose, icrrad)
# w = DD.angular_velocity_given_wheel_velocities(vr, vl, l)
# vr, vl = DD.wheel_velocities(w, icrrad, l) 
# icr = DD.icr_given_pose_and_icr_radius(pose, icrrad)
# v = DD.velocity_given_wheel_velocities(vr, vl)
# print()

# KINEMATICS
# rotangle = w * 2
# pose = pose.rotate_around_point(rotangle, icr)
# print(pose)

# WHEEL VELOCITIES
# ww = 0
# wv = 0
# wr = 0
# ww = DD.wheel_angular_velocity_given_linear_and_radius(wv, wr)
# wv = DD.wheel_linear_velocity_given_angular_and_radius(ww, wr)
# wr = DD.wheel_radius_given_linear_and_angular_velocity(wv, ww)