from threading import Thread

from first_step.Drone import DronesFactory
from first_step.PointClout import PointCloud
from first_step.tools.MeasurmentHelper import measurments_to_points
from first_step.tools.Reporter import Reporter
from first_step.tools.SaveDataHelper import save_points_to_file


class SwarmController:
    def __init__(self, uris):
        self.point_cloud = PointCloud(save_points_to_file)
        self.drones = DronesFactory(self.on_new_data).construct(uris)

    def on_new_data(self, timestamp, data, config):
        new_points = measurments_to_points(data["measurement"], data["pos"])
        self.point_cloud.add(new_points)

    def _take_off_and_scan_around(self, drone):
        print("take_off")
        drone.take_off()
        print("scan")
        drone.scan_around()
        print("land")
        drone.land()
        drone.disconnect()

    def take_off_and_scan_around(self):
        self._parallel_safe(self._take_off_and_scan_around, )

    def _parallel_safe(self, func, args_dict=None):
        """
        Execute a function for all Crazyflies in the swarm, in parallel.
        One thread per Crazyflie is started to execute the function. The
        threads are joined at the end and if one or more of the threads raised
        an exception this function will also raise an exception.

        For a more detailed description of the arguments, see `sequential()`

        :param func: The function to execute
        :param args_dict: Parameters to pass to the function
        """
        threads = []
        reporter = Reporter()

        for drone in self.drones:
            args = [func, reporter] + [drone]

            thread = Thread(target=self._thread_function_wrapper, args=args)
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        if reporter.is_error_reported():
            first_error = reporter.errors[0]
            raise Exception('One or more threads raised an exception when '
                            'executing parallel task') from first_error

    def _process_args_dict(self, scf, uri, args_dict):
        args = [scf]

        if args_dict:
            args += args_dict[uri]

        return args

    def _thread_function_wrapper(self, *args):
        reporter = None
        try:
            func = args[0]
            reporter = args[1]
            func(args[2])
        except Exception as e:
            if reporter:
                reporter.report_error(e)


