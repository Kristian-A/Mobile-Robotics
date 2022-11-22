from src.coordinates import Point
import numpy as np

class DifferentialDrive:  
    def icr_given_pose_and_icr_radius(pose, icr_radius):
        normal_icr = Point(-np.sin(pose.theta), np.cos(pose.theta))
        return Point(pose + normal_icr * icr_radius)
        
    def icr_radius_given_wheel_velocities(velocity_right, velocity_left, axle_lenght):
        result = 0.5 * axle_lenght * (velocity_right + velocity_left) / np.abs(velocity_right - velocity_left)
        return float(result)
    
    def icr_radius_given_velocity_and_angular(velocity, angular):
        return velocity / angular
    
    def velocity_given_wheel_velocities(velocity_right, velocity_left):
        return (velocity_right + velocity_left) / 2
    
    def velocity_given_angular_velocity_and_icr_radius(angular_velocity, icr_radius):
        return angular_velocity * icr_radius
    
    def angular_velocity_given_wheel_velocities(velocity_right, velocity_left, axle_lenght):
        return (velocity_right - velocity_left) / axle_lenght
    
    def wheel_velocities(angular_velocity, icr_radius, axle_length):
        left  = angular_velocity * (icr_radius - axle_length / 2)
        right = angular_velocity * (icr_radius + axle_length / 2)
        return (right, left)
    
    def wheel_angular_velocity_given_linear_and_radius(wheel_linear_velocity, wheel_radius):
        return wheel_linear_velocity / wheel_radius
    
    def wheel_linear_velocity_given_angular_and_radius(wheel_angular_velocity, wheel_radius):
        return wheel_angular_velocity * wheel_radius
        
    def wheel_radius_given_linear_and_angular_velocity(wheel_linear_velocity,  wheel_angular_velocity):
        return wheel_linear_velocity / wheel_angular_velocity