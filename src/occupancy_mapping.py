import numpy as np

class OccupancyMapping:
    def __init__(self, robot_pose, point):
        self.robot_pose = robot_pose
        self.point = point
        self.radius = self.get_radius()
        self.bearing = self.get_bearing()

    def get_radius(self):
        return (self.point - self.robot_pose).l2_norm()

    def get_bearing(self):
        x_diff, y_diff = (self.point - self.robot_pose).tuple()
        return np.arctan2(y_diff, x_diff) - self.robot_pose.theta

    def get_closest_sensor_index(self, sensor_orientations):
        sensors_bearings_diffs = np.abs(sensor_orientations - self.bearing)
        return np.argmin(sensors_bearings_diffs)

    def in_region1(self, sensor_range):
        return self.radius < sensor_range

    def in_region2(self, sensor_range, sensor_reading, sensor_depth):
        return sensor_reading < sensor_range and np.abs(self.radius-sensor_reading) < sensor_depth / 2

    def in_region3(self, sensor_range, sensor_reading, sensor_depth, cone_width, sensor_orientation):
        diff = np.abs(sensor_orientation - self.bearing)
        return self.radius > min(sensor_range, sensor_reading + 0.5 * sensor_depth) or diff > 0.5 * cone_width

    def get_region(self, sensor_range, sensor_reading, sensor_depth, cone_width, sensor_orientation):
    
        if self.in_region3(sensor_range, sensor_reading, sensor_depth, cone_width, sensor_orientation):
            print("Region 3")
            return

        if self.in_region1(sensor_range):
            print("Region 1")
            return
        
        if self.in_region2(sensor_range, sensor_reading, sensor_depth):
            print("Region 2")
            return

        print("You suck! 😛😘")

class LogMap:
    def __init__(self, probability, prior = 0.5):
        self.log_odds = LogMap.get_log_odds(probability)
        self.prior = LogMap.get_log_odds(prior)
        self.total = 0
        
    def observed_occupied(self, count):
        self.total += (self.log_odds - self.prior) * count

    def observed_non_occupied(self, count):
        self.total += (-self.log_odds - self.prior) * count

    def get_result(self):
        return self.total
    
    def get_probability(self):
        1 - (1 / (1 + np.exp(self.total)))
        
    @staticmethod
    def get_log_odds(probability):
        return np.log(probability / (1 - probability))
        