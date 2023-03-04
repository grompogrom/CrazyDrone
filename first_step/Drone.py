import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.utils.callbacks import Caller

from first_step.Loger import Logger
from first_step.MotionCommander import MotionCommander


class Drone:
    def __init__(self, drone_uri, meas_listener=None):
        cflib.crtp.init_drivers()
        self.uri = drone_uri
        self.scf = SyncCrazyflie(drone_uri)
        self.commander = MotionCommander(self.scf.cf)
        self.on_data_received = Caller()
        self.scf.open_link()
        self.logger = Logger(self.scf.cf.log)
        self.logger.add_pos_listener(self.pos_data_cb)
        self.logger.add_measurement_listener(self.meas_data_cb)
        if meas_listener is not None:
            self.on_data_received.add_callback(meas_listener)
        self.logger.start_logging()

        self.position = []

    def take_off(self):
        self.commander.take_off()

    def land(self):
        self.commander.land()

    def scan_around(self):
        self.commander.rotate_right(90)

    def pos_data_cb(self, timestamp, data, logconf):
        self.position = [
            data['stateEstimate.x'],
            data['stateEstimate.y'],
            data['stateEstimate.z']
        ]

    def meas_data_cb(self, timestamp, data, logconf):
        measurement = {
            'roll': data['stabilizer.roll'],
            'pitch': data['stabilizer.pitch'],
            'yaw': data['stabilizer.yaw'],
            'front': data['range.front'],
            'back': data['range.back'],
            'up': data['range.up'],
            'down': data['range.zrange'],
            'left': data['range.left'],
            'right': data['range.right']
        }
        self.on_data_received.call(timestamp, {"measurement": measurement, "pos": self.position}, logconf)

    def disconnect(self):
        self.scf.close_link()

    def calibrate(self):
        pass


class DronesFactory:
    def __init__(self, measurement_listener):
        self._measurement_listener = measurement_listener

    def construct(self, uris):
        return [Drone(uri, self._measurement_listener) for uri in uris]



if __name__ == "__main__":
    URI1 = "radio://0/120/2M/E7E7E7E7E5"
    drone = Drone(URI1, lambda t, d, l: print(d))
    drone.take_off()
    drone.commander.rotate_right(300)
    time.sleep(2)
    drone.land()
    drone.disconnect()
