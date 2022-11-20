from coordinates import Pose, Point
import numpy as np


class ScanSensorModel:
    def get_rel_sensor_poses(self, radius: float | np.float_, rotation_angle_rad: float | np.float_, sensor_count: int = -1):
        if sensor_count == -1:
            sensor_count = int(2*np.pi / rotation_angle_rad)
        sensor_0 = Pose(radius, 0, 0)
        return [sensor_0.rotate(rotation_angle_rad * i) for i in range(sensor_count)]

    def get_abs_sensor_pose(self, robot_pose: Pose, sensor_pose: Pose):
        sensor_point = Point(sensor_pose)
        rotated_sensor_point = Pose(sensor_point.rotate_point(robot_pose.theta), sensor_pose.theta)
        return rotated_sensor_point + robot_pose
    
    def get_reading_location(self, abs_sensor_pose: Pose, distance: float | np.float_):
        result = abs_sensor_pose.tuple() + distance * np.array([np.cos(abs_sensor_pose.theta), np.sin(abs_sensor_pose.theta)])
        return Point(result[0], result[1])     

ssm = ScanSensorModel() 
interest_s = ssm.get_rel_sensor_poses(0.1, np.pi / 3)[2]
robot_pose = Pose(2.0, 3.0, np.pi/6)
abs_sense = ssm.get_abs_sensor_pose(robot_pose, interest_s)
# print(ssm.get_reading_location(abs_sense, 10))
