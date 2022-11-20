from coordinates import *
import numpy as np

class DifferentialDrive:  
    def icr(self, pose: Pose, icr_radius: float) -> Point:
        normal_icr = Point(-np.sin(pose.theta), np.cos(pose.theta))
        return Point(pose + normal_icr * icr_radius)
        
    def icr_radius_given_wheel_velocities(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        result = 0.5 * axle_lenght * (velocity_right + velocity_left) / np.abs(velocity_right - velocity_left)
        return float(result)
    
    def icr_radius_given_velocity_and_angular(self, velocity: float, angular: float) -> float:
        return velocity / angular
    
    def velocity_given_wheel_velocities(self, velocity_right: float, velocity_left: float):
        return (velocity_right + velocity_left) / 2
    
    def velocity_given_angular_velocity_and_icr_radius(self, angular_velocity: float, icr_radius: float):
        return angular_velocity * icr_radius
    
    def angular_velocity_given_wheel_velocities(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        return (velocity_right - velocity_left) / axle_lenght
    
    def wheel_velocities(self, angular_velocity: float, icr_radius: float, axle_length: float):
        left  = angular_velocity * (icr_radius - axle_length / 2)
        right = angular_velocity * (icr_radius + axle_length / 2)
        return (right, left)
   
dd = DifferentialDrive()

vl = np.pi
vr = 2*np.pi
l = 3

r = dd.icr_radius_given_wheel_velocities(vr, vl, l)
w = dd.angular_velocity_given_wheel_velocities(vr, vl, l)
v = dd.velocity_given_angular_velocity_and_icr_radius(w, r)

# print(v/np.pi)