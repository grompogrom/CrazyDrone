from cflib.crazyflie.log import LogConfig, Log


class Logger:

    def __init__(self, loger: Log):
        self.logger = loger
        self.pos_config = self._create_pos_config()
        self.measurment_config = self._create_measurement_config()
        self.logger.add_config(self.pos_config)
        self.logger.add_config(self.measurment_config)
        pass

    def start_logging(self):
        self.pos_config.start()
        self.measurment_config.start()

    def add_pos_listener(self, listener):
        self.pos_config.data_received_cb.add_callback(listener)

    def add_measurement_listener(self, listener):
        self.measurment_config.data_received_cb.add_callback(listener)

    def _create_pos_config(self):
        lpos = LogConfig(name='Position', period_in_ms=50)
        lpos.add_variable('stateEstimate.x')
        lpos.add_variable('stateEstimate.y')
        lpos.add_variable('stateEstimate.z')
        return lpos

    def _create_measurement_config(self):
        lmeas = LogConfig(name='Meas', period_in_ms=50)
        lmeas.add_variable('range.front')
        lmeas.add_variable('range.back')
        lmeas.add_variable('range.up')
        lmeas.add_variable('range.left')
        lmeas.add_variable('range.right')
        lmeas.add_variable('range.zrange')
        lmeas.add_variable('stabilizer.roll')
        lmeas.add_variable('stabilizer.pitch')
        lmeas.add_variable('stabilizer.yaw')
        return lmeas
