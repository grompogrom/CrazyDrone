from datetime import time

import cflib
from cflib.crazyflie.swarm import CachedCfFactory, Swarm
from cflib.positioning.motion_commander import MotionCommander
from cflib.utils import uri_helper

def unit_controller():
 uri_1 = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
 uri_2 = uri_helper.uri_from_env(default='radio://0/80/2M/E7E7E7E7E7')
 uris = {uri_1,uri_2}

 swarm = Swarm(uris)
 swarm.open_links(uris[0],uris[1])
 commander = MotionCommander(swarm)
 commander.take_off()
 commander.up(1)
 time.sleep(5)
 swarm.sequential(lambda commander: commander.down(0.3))
 swarm.sequential(lambda commander: commander.up(0.3))
 time.sleep(2)
 commander.land(0.2)

if __name__ == '__main__':
    cflib.crtp.init_drivers()
    unit_controller()



