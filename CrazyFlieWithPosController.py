
from cflib.crazyflie import Crazyflie
from cflib.crazyflie.syncCrazyflie import SyncCrazyflie
from cflib.positioning.position_hl_commander import PositionHlCommander


class CrazyFlieWithPosController(Crazyflie):
	def __init__(self, link, ro_cache, rw_cache):
		super().__init__(link, ro_cache, rw_cache)
		self.positionCommander = PositionHlCommander(self)


class PosControllerCfFactory:
    """
    Factory class that creates Crazyflie instances with TOC caching
    to reduce connection time.
    """

    def __init__(self, ro_cache=None, rw_cache=None):
        self.ro_cache = ro_cache
        self.rw_cache = rw_cache

    def construct(self, uri):
        cf = CrazyFlieWithPosController(ro_cache=self.ro_cache, rw_cache=self.rw_cache)
        return SyncCrazyflie(uri, cf=cf)
