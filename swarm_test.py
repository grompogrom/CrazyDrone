import time
import cflib.crtp
from cflib.crazyflie import HighLevelCommander
from cflib.crazyflie.swarm import CachedCfFactory
from cflib.crazyflie.swarm import Swarm



def activate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 255)

def deactivate_led_bit_mask(scf):
    scf.cf.param.set_value('led.bitmask', 0)

def light_check(scf):
    activate_led_bit_mask(scf)
    time.sleep(2)
    deactivate_led_bit_mask(scf)
    time.sleep(2)

def take_off(scf):
    print('take off')
    commander= scf.cf.high_level_commander
    commander.takeoff(1.0, 2.0)
    time.sleep(3)


def land(scf):
    print('land')
    commander: HighLevelCommander= scf.cf.high_level_commander
    commander.land(absolute_height_m=0, duration_s=4)
    time.sleep(5)
    commander.stop()

#Function swap position
def swap_positions(scf):
  take_off(scf)
  time.sleep(3)

 #////////////////////////////////

def mask_up(scf):


def hover_sequence(scf):
    take_off(scf)
    time.sleep(3)
    change_position(scf)
    time.sleep(3)
    rotate(scf)
    time.sleep(3)
    land(scf)

def change_position(scf):
    commander: HighLevelCommander= scf.cf.high_level_commander
    commander.go_to(1,0,1,0,3)
    time.sleep(3)

def rotate(scf):
    commander: HighLevelCommander= scf.cf.high_level_commander
    commander.go_to(0,0,0,90,2,True)


uris = {
    #'radio://0/110/2M/E7E7E7E7E3',
    'radio://0/110/2M/E7E7E7E7E9',
    'radio://0/80/2M/E7E7E7E7E7',
    #'radio://0/80/2M/E7E7E7E7E8'

    # 'radio://0/20/2M/E7E7E7E704',
    # Add more URIs if you want more copters in the swarm
}

group_mask = {
'radio://0/110/2M/E7E7E7E7E9'
}

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    factory = CachedCfFactory(rw_cache='./cache')
    with Swarm(uris, factory=factory) as swarm:
        print('Connected to  Crazyflies')
        # swarm.parallel_safe(light_check)
        swarm.reset_estimators()
        print('estimators reseted')
        swarm.parallel(swap_positions)


