import time

import cflib
from cflib.crazyflie import HighLevelCommander
from cflib.crazyflie.swarm import Swarm, CachedCfFactory
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie

from beautiful_flie.coords_caster import CoordsCaster
from beautiful_flie.trajectory import uris, takeoff_land, figure_1, figure_2, figure_3

converter = CoordsCaster([5.53, 5.57], 2,2)

def change_position(scf: SyncCrazyflie, params: dict):
	x, y, z, t = list(params.values())
	commander: HighLevelCommander= scf.cf.high_level_commander
	x,y,z = converter.cast_coords(x,y,z)
	commander.go_to(x,y,z,0,t)
	time.sleep(t)


def take_off(scf: SyncCrazyflie, params):
	z, t = params['z'], params['t']
	commander: HighLevelCommander = scf.cf.high_level_commander
	commander.takeoff(z, t)
	time.sleep(3)


def land(scf):
	commander: HighLevelCommander = scf.cf.high_level_commander
	commander.land(0, 4)
	time.sleep(3)


if __name__ == "__main__":
	cflib.crtp.init_drivers()
	factory = CachedCfFactory(rw_cache='./cache')
	with Swarm(uris, factory=factory) as swarm:
		print('Connected to  Crazyflies')
		swarm.reset_estimators()
		print('estimators reseted')
		swarm.parallel_safe(take_off, takeoff_land)
		# swarm.parallel_safe(change_position, takeoff_land)
		for i in range(3):
			swarm.parallel_safe(change_position, figure_1)
			time.sleep(2)
			swarm.parallel_safe(change_position, figure_2)
			time.sleep(2)
			swarm.parallel_safe(change_position, figure_3)
			time.sleep(2)

		time.sleep(2)
		swarm.parallel_safe(land)