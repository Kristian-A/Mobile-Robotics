from __future__ import annotations

import numpy as np


"""
See answer lower in the responses:
https://stackoverflow.com/questions/33533148/how-do-i-type-hint-a-method-with-the-type-of-the-enclosing-class/33533514#33533514
"""

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
    
    def to_array_like(self) -> np.ndarray:
        return np.array([self.x, self.y])
    
    def rotate(self, theta: float) -> Point:
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        result = rotation_matrix.dot(self.to_array_like())
        return Point(result[0], result[1])
    
    @staticmethod
    def from_pose(pose: Pose) -> Point:
        return Point(pose.x, pose.y)
    
    def __mul__(self, num: float) -> Point:
        return Point(self.x * num, self.y * num)
    
    def __str__(self):
        return f'({self.x}, {self.y})'
    
    def __add__(self, point: Point) -> Point:
        return Point(self.x + point.x, self.y + point.y)
    
class Pose(Point):
    def __init__(self, x, y, theta) -> None:
        super().__init__(x, y)
        self.theta = theta
        
    def rotate(self, rotation_angle: float, icr: Point) -> Pose:
        translated_point = Point.from_pose(self - icr)
        rotated_point = translated_point.rotate(rotation_angle)
        result_point = rotated_point + icr
        return Pose.from_point(result_point, rotation_angle + self.theta)
    
    @staticmethod
    def from_point(point: Point, theta: float) -> Pose:
        return Pose(point.x, point.y, theta)
    
    def __add__(self, object: Point | Pose) -> Point | Pose:
        if type(object) is Point:
            return Pose(self.x + object.x, self.y + object.y, self.theta) 
            
        if type(object) is Pose:
            return Pose(self.x + object.x, self.y + object.y, self.theta + object.theta)
        
        raise Exception()
    
    def __sub__(self, point: Point) -> Pose :
        return Pose(self.x - point.x, self.y - point.y, self.theta)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.theta})'

class DifferentialDrive:  
    # NOTE-TD: I really didn't like the previous implementation of the function. I find this a lot cleaner.
    def get_icr(self, pose: Pose, icr_radius: float) -> Pose:
        x_icr = pose.x - icr_radius * np.sin(pose.theta)
        y_icr = pose.y +  icr_radius * np.cos(pose.theta)
        return Pose(x_icr, y_icr, pose.theta)
        
    def get__velocity_given_wheel(self, velocity_right: float, velocity_left: float):
        return (velocity_right + velocity_left) / 2
    
    def get_velocity_given_angular(self, angular_velocity: float, icr_radius: float):
        return angular_velocity * icr_radius
     
    def get_radius(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        return 0.5 * axle_lenght * (velocity_right + velocity_left) / np.abs(velocity_right - velocity_left)
    
    def get_angular(self, velocity_right: float, velocity_left: float, axle_lenght: float):
        return (velocity_right - velocity_left) / axle_lenght
        
    def get_wheel_velocities(self, angular_velocity: float, icr_radius: float, axle_length: float):
        left  = angular_velocity * (icr_radius - axle_length/2)
        right = angular_velocity * (icr_radius + axle_length/2)
        return (left, right)
    

diff_drive = DifferentialDrive()
pose = Pose(6, 2, np.radians(120))

icr_radius = diff_drive.get_radius(3*np.pi, 2*np.pi, 4)
icr = diff_drive.get_icr(pose, icr_radius)
angular_velocity = diff_drive.get_angular(3*np.pi, 2*np.pi, 4)

final_pose = pose.rotate(angular_velocity*2, icr)
print(final_pose)