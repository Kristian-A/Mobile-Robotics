from __future__ import annotations
import numpy as np

class Point:
    def __init__(self, *args) -> None:
        if type(args[0]) is float or type(args[0]) is np.float_:
            self.x = args[0]
            self.y = args[1]
            return
        if type(args[0]) is Point or type(args[0]) is Pose:
            other = args[0]
            self.x = other.x
            self.y = other.y
            return
    
    def _rotate(self, theta: float) -> Point:
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        result = rotation_matrix.dot(self.__tuple())
        return Point(result[0], result[1])
    
    def __tuple(self) -> np.ndarray:
        return (self.x, self.y)

    def __mul__(self, object: float | Point) -> Point:
        if type(object) is float:
            return Point(self.x * object, self.y * object)
        if type(object) is Point:
            return Point(self.x * object.x, self.y * object.y)
        raise Exception('Multiplication with Point requires Point or float')

    def __add__(self, point: Point) -> Point:
        return Point(self.x + point.x, self.y + point.y)

    def __str__(self):
        return f'({self.x}, {self.y})'
    
class Pose(Point):
    def __init__(self, *args) -> None:
        super().__init__(*args)
        if type(args[0]) is float or type(args[0]) is np.float_:
            self.theta = args[-1]
            return
        if type(args[0]) is Pose:
            self.theta = pose.theta
            return
        if type(args[0]) is Point:
            self.theta = args[-1]        
            return

    def rotate(self, rotation_angle: float, icr: Point) -> Pose:
        translated_point = Point(self - icr)
        rotated_point = translated_point._rotate(rotation_angle)
        result_point = rotated_point + icr
        return Pose(result_point, rotation_angle + self.theta)
    
    def __add__(self, object: Pose | Point) -> Pose:
        if type(object) is Pose:
            return Pose(self.x + object.x, self.y + object.y, self.theta + object.theta)
        if type(object) is Point:
            return Pose(self.x + object.x, self.y + object.y, self.theta) 
        raise Exception('Addition with Pose requires another Pose or Point')

    def __sub__(self, point: Point) -> Pose :
        return Pose(self.x - point.x, self.y - point.y, self.theta)

    def __str__(self):
        return f'({self.x}, {self.y}, {self.theta})'

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

icr_radius = diff_drive.get_radius(3*np.pi, 2*np.pi, 4)
print(icr_radius)
icr = diff_drive.get_icr(pose, icr_radius)
angular_velocity = diff_drive.get_angular(3*np.pi, 2*np.pi, 4)
final_pose = pose.rotate(angular_velocity*2, icr)

print(final_pose)