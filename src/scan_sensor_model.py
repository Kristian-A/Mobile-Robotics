import numpy as np
from src.coordinates import Pose, Point
from src.probability_calculator import ProbabilityUtility

class ScanSensorModel:
    def get_rel_sensor_poses(radius, rotation_angle_rad, sensor_count = -1):
        if sensor_count == -1:
            sensor_count = int(2*np.pi / rotation_angle_rad)
        sensor_0 = Pose(radius, 0, 0)
        return [sensor_0.rotate(rotation_angle_rad * i) for i in range(sensor_count)]

    def get_abs_sensor_pose(robot_pose, sensor_pose):
        sensor_point = Point(sensor_pose)
        rotated_sensor_point = Pose(sensor_point.rotate_point(robot_pose.theta), sensor_pose.theta)
        return rotated_sensor_point + robot_pose

    def get_reading_location(global_sensor_pose, distance):
        result = global_sensor_pose.tuple() + distance * np.array([np.cos(global_sensor_pose.theta), np.sin(global_sensor_pose.theta)])
        return Point(result[0], result[1])  
    
    def get_reading_likelihood(landmark_point, sensor_point, measured_distance, std, distribution = ProbabilityUtility.triangular):
        actual_distance = (landmark_point - sensor_point).l2_norm()
        return distribution(measured_distance - actual_distance, std)
    
    def trilateration(point_1, point_2, radius_1, radius_2):
        d = (point_1 - point_2).l2_norm()
        x = (d**2 - radius_1**2 + radius_2**2) / 2*d
        y = np.sqrt(radius_1**2 - x**2)
        return np.array([(x, y), (x, -y)])
        
        