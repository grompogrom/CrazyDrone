import logging
import sys
import time
from threading import Event

import cflib.crtp
from cflib.crazyflie import Crazyflie, HighLevelCommander
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

URI = uri_helper.uri_from_env(default="radio://0/80/2M/E7E7E7E7E2")

DEFAULT_HEIGHT = 1

logging.basicConfig(level=logging.ERROR)

def take_off_simple(scf):
    commander:HighLevelCommander = scf.cf.high_level_commander
    commander.takeoff(1,1)
    commander.go_to(0,0,0.3, 0,1, True)
    time.sleep(10)
    commander.land(0, 1)



if __name__ == '__main__':
    cflib.crtp.init_drivers()

    with SyncCrazyflie(URI, cf=Crazyflie(rw_cache='./cache')) as scf:

        time.sleep(1)

        take_off_simple(scf)