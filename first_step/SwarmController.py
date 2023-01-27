from first_step.Drone import DronesFactory
from first_step.PointClout import PointCloud
from first_step.tools.MeasurmentHelper import measurments_to_points
from first_step.tools.SaveDataHelper import save_points_to_file


class SwarmController:
    def __init__(self, uris):
        self.point_cloud = PointCloud(save_points_to_file)
        self.drones = DronesFactory(self.on_new_data).construct(uris)

    def on_new_data(self, timestamp, data, config):
        new_points = measurments_to_points(data["measurement"], data["pos"])
        self.point_cloud.add(new_points)

    def take_off_and_scan_around(self):
        for drone in self.drones:
            drone.take_off()
            drone.scan_around()
            drone.land()
            drone.disconnect()


