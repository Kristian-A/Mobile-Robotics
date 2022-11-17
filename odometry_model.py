from coordinates import Pose
import numpy as np
import fractions

class Odometry:
    def __init__(self, rotation_start, translation, rotation_end) -> None:
        self.rotation_start = rotation_start
        self.translation = translation
        self.rotation_end = rotation_end
        
    def __str__(self):
        trans = np.around(self.translation, 6)
        rot_start_pi = fractions.Fraction(self.rotation_start / (np.pi)).limit_denominator()
        rot_end_pi = fractions.Fraction(self.rotation_end / (np.pi)).limit_denominator()
        rot_start_deg = np.degrees(self.rotation_start)
        rot_end_deg = np.degrees(self.rotation_end)
        
        ret = 'Odometry:\n'
        ret += f'\trot_start = {self.rotation_start} = {rot_start_pi}π = {rot_start_deg}°\n'
        ret += f'\ttranslation = {trans}\n'
        ret += f'\trot_end = {self.rotation_end} = {rot_end_pi}π = {rot_end_deg}°\n'
        return ret

class OdometryMotionModel:
    def odometry(self, pose_start: Pose, pose_end: Pose):
        diff = pose_end - pose_start  
        rotation_start = Pose.atan2(pose_start, pose_end) - pose_start.theta
        translation = diff.l2_norm()
        rotation_end = diff.theta - rotation_start
        return Odometry(rotation_start, translation, rotation_end)



model = OdometryMotionModel()



# pose_start = Pose(5.0, 3.0, np.pi/6)
# pose_end = Pose(8.0, 7.0, np.pi * 5 / 6)
# print(model.odometry(pose_start, pose_end))