import time

import cflib.crtp
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

from CrazyLogger import CrazyLogger, create_lg_stab

uri = uri_helper.uri_from_env(default="radio://0/110/2M/E7E7E7E7E8")




def simple_connect(scf):
    print("Yeah, I'm connected! :D")
    with MotionCommander(scf) as motion_controller:
        motion_controller.up(1)
        motion_controller.circle_right(1.0, 1.6)

    # time.sleep(9)
    # scf.cf.high_level_commander.go_to(0.5, 0.5, 2.3, 0, 3)
    time.sleep(5)
    # scf.cf.high_level_commander.go_to(2.7, 4, 2, 0, 5)
    # time.sleep(7)
    # scf.cf.high_level_commander.land(0,6)
    # time.sleep(6)



if __name__ == '__main__':
    # Initialize the low-level drivers
    cflib.crtp.init_drivers()
    with SyncCrazyflie(uri, cf=CrazyLogger(create_lg_stab(),rw_cache='./cache')) as scf:
        simple_connect(scf)
