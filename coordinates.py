from __future__ import annotations
import numpy as np
import fractions

class Point:
    def __init__(self, *args) -> None:
        if type(args[0]) in [float, np.float_, int]:
            self.x = args[0]
            self.y = args[1]
            return
        if type(args[0]) in [Point, Pose]:
            other = args[0]
            self.x = other.x
            self.y = other.y
            return
    
    def rotate_point(self, theta: float) -> Point:
        rotation_matrix = np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
        result = rotation_matrix.dot(self.tuple())
        return Point(result[0], result[1])
    
    def tuple(self) -> np.ndarray:
        return (self.x, self.y)

    def l2_norm(self) -> np.float_:
        return np.linalg.norm(self.tuple())

    def __mul__(self, object: float | Point) -> Point:
        if type(object) is float:
            return Point(self.x * object, self.y * object)
        if type(object) is Point:
            return Point(self.x * object.x, self.y * object.y)
        raise Exception('Multiplication with Point requires Point or float')

    def __add__(self, object: float | np.float_ | Point | Pose) -> Point:
        if type(object) in [float, np.float_]:
            return Point(self.x + object, self.y + object)
        if type(object) is Pose:
            return object + self
        return Point(self.x + object.x, self.y + object.y)

    def __sub__(self, object: float | np.float_ | Pose | Point) -> Pose | Point:
        if type(object) in [float, np.float_]:
            return Point(self.x + object, self.y + object)
        if type(object) is Pose:
            return Pose(self.x - object.x, self.y - object.y, object.theta)
        if type(object) is Point:
            return Point(self.x - object.x, self.y - object.y) 
        raise Exception('Addition with Pose requires another Pose or Point')

    def __str__(self):
        return f'(x={self.x}, y={self.y})'


class Pose(Point):
    @staticmethod
    def atan2(pose_start: Pose, pose_end: Pose) -> np.float_:
        diff = pose_end - pose_start
        return np.arctan2(diff.y, diff.x)

    def __init__(self, *args) -> None:
        super().__init__(*args)

        if type(args[0]) is Pose:
            self.theta = args[0].theta
            return
        if type(args[0]) in [float, np.float_, Point, int]:
            self.theta = args[-1]
            return

    def rotate_around_point(self, rotation_angle: float, point: Point) -> Pose:
        translated_point = Point(self - point)
        rotated_point = translated_point._rotate(rotation_angle)
        result_point = rotated_point + point
        return Pose(result_point, rotation_angle + self.theta)
    
    def rotate(self, rotation_angle: float) -> Pose:
        point = Point(self)
        rotated_point = point.rotate_point(rotation_angle + self.theta)
        return Pose(rotated_point, rotation_angle + self.theta)
        
    def __add__(self, object: float | np.float_ | Pose | Point) -> Pose:
        if type(object) is Pose:
            return Pose(self.x + object.x, self.y + object.y, self.theta + object.theta)
        if type(object) is Point:
            return Pose(self.x + object.x, self.y + object.y, self.theta) 
        raise Exception('Addition with Pose requires another Pose or Point')

    def __sub__(self, object: float | np.float_ | Pose | Point) -> Pose :
        if type(object) in [float, np.float_]:
            return Pose(self.x + object, self.y + object, self.theta + object)
        if type(object) is Pose:
            return Pose(self.x - object.x, self.y - object.y, self.theta - object.theta)
        if type(object) is Point:
            return Pose(self.x - object.x, self.y - object.y, self.theta) 
        raise Exception('Addition with Pose requires another Pose or Point')

    def __str__(self):
        x_r, y_r, theta_r = np.around([self.x, self.y, self.theta], 6)
        theta_pi = fractions.Fraction(self.theta / (np.pi)).limit_denominator()
        theta_degrees = np.degrees(self.theta)
        return f'(x={x_r}, y={y_r}, theta={theta_r}=({theta_pi})π={theta_degrees}°)'
    