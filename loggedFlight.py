import logging
import time

import cflib.crtp
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from cflib.crazyflie.log import LogConfig
from cflib.crazyflie.syncLogger import SyncLogger
from cflib.positioning.motion_commander import MotionCommander

# URI to the Crazyflie to connect to
uri = 'radio://0/80/2M/E7E7E7E7E7'

# Only output errors from the logging framework
logging.basicConfig(level=logging.ERROR)

x = 0
y = 0
z = 0

logs = {
    'stateEstimate.x': x,
    'stateEstimate.y': y,
    'stateEstimate.z': z
}


def log_stab_callback(timestamp, data, logconf):
    print('[%d][%s]: %s' % (timestamp, logconf.name, data))
    if logconf.name in logs.keys():
        logs[logconf.name] = data


def update_log_data(scf):
    logconf = LogConfig(name='Stabilizer', period_in_ms=10)
    for log_name in logs.keys():
        logconf.add_variable(log_name, 'float')
    cf = scf.cf
    cf.log.add_config(logconf)
    logconf.data_received_cb.add_callback(log_stab_callback)
    logconf.start()
    time.sleep(2)
    logconf.stop()


if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()

    lg_stab = LogConfig(name='Stabilizer', period_in_ms=10)
    lg_stab.add_variable('stateEstimate.x', 'float')
    lg_stab.add_variable('stateEstimate.y', 'float')
    lg_stab.add_variable('stateEstimate.z', 'float')
    lg_stab.add_variable('stabilizer.roll', 'float')
    lg_stab.add_variable('stabilizer.pitch', 'float')
    lg_stab.add_variable('stabilizer.yaw', 'float')
    # The fetch-as argument can be set to FP16 to save space in the log packet
    lg_stab.add_variable('pm.vbat', 'FP16')

    def simple_connect(scf):
        print("Yeah, I'm connected! :D")
        motion_controller = MotionCommander(scf)
        motion_controller.take_off(height=1)
        motion_controller.up(1)
        # motion_controller.left(0.5)
        time.sleep(3)
        motion_controller.land()
    with SyncCrazyflie(uri, cf=Crazyflie(rw_cache='./cache')) as scf:

        update_log_data(scf, lg_stab)
        simple_connect(scf)
