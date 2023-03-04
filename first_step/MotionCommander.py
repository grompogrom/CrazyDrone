from cflib.positioning.motion_commander import MotionCommander as CrazyFlieCommander


class MotionCommander:
    def __init__(self, cf, default_height=0.3):
        self.cf_commander = CrazyFlieCommander(cf, default_height)

    def take_off(self):
        self.cf_commander.take_off()

    def rotate_right(self, angle):
        self.cf_commander.turn_right(angle, 20)

    def land(self):
        self.cf_commander.land()