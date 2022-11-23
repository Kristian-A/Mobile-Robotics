import numpy as np
from src.coordinates import Pose, Point
from src.occupancy_mapping import LogMap as LM, OccupancyMapping as OM

## OCCUPANCY MAPPING SECTIONS
# robot_pose = Pose(2.0, 3.0, np.pi / 6)
# map_point = Point(5.0, 6.0)

# sensor_range = 5.0
# sensor_depth = 1.0
# cone_width = 0.593
# sensor_count = 4
# sensor_orientations = [np.pi / 2  * k for k in range(0, sensor_count)]
# sensor_reading = 4.0

# mapp = OM(robot_pose, map_point)
# bearing = mapp.get_bearing()
# radius = mapp.get_radius()
# closest_sensor_idx = mapp.get_closest_sensor_index(sensor_orientations)
# closest_sensor_orientation = sensor_orientations[closest_sensor_idx]
# mapp.get_region(sensor_range, sensor_reading, sensor_depth, cone_width, closest_sensor_orientation)


# LOG MAP
# logmap = LM(0.8)
# logmap.observed_occupied(3)
# logmap.observed_non_occupied(1)
# # print(logmap.get_result())