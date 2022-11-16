from __future__ import annotations
import numpy as np
from coordinates import *

class DifferentialDrive:  
    def get_icr(self, pose: Pose, icr_radius: float) -> Pose:
        normal_icr = Point(-np.sin(pose.theta), np.cos(pose.theta))
        return pose + normal_icr * icr_radius
    
    def get_icr2(self, pose: Pose, icr_radius: float) -> Pose:
        x_icr = pose.x - icr_radius * np.sin(pose.theta)
        y_icr = pose.y + icr_radius * np.cos(pose.theta)
        return Pose(x_icr, y_icr, pose.theta)
        
    def get__velocity_given_wheel(self, velocity_right: float, velocity_left: float):
        return (velocity_right + velocity_left) / 2
    
    def get_velocity_given_angular(self, angular_velocity: float, icr_radius: float):
        return angular_velocity * icr_radius
     
    def get_radius(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        result = 0.5 * axle_lenght * (velocity_right + velocity_left) / np.abs(velocity_right - velocity_left)
        return float(result)
    
    def get_angular(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        return (velocity_right - velocity_left) / axle_lenght
        
    def get_wheel_velocities(self, angular_velocity: float, icr_radius: float, axle_length: float):
        left  = angular_velocity * (icr_radius - axle_length/2)
        right = angular_velocity * (icr_radius + axle_length/2)
        return (left, right)
    
diff_drive = DifferentialDrive()

pose = Pose(6.0, 2.0, np.radians(120))
pose2 = Pose(6.0, 3.0, np.radians(120))
point = Point(7.0, 2.0)

print(pose + pose2)

# icr_radius = diff_drive.get_radius(3*np.pi, 2*np.pi, 4)
# print(icr_radius)
# icr = diff_drive.get_icr(pose, icr_radius)
# angular_velocity = diff_drive.get_angular(3*np.pi, 2*np.pi, 4)
# final_pose = pose.rotate(angular_velocity*2, icr)

# print(final_pose)