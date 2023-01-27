from first_step.SwarmController import SwarmController
import numpy as np
import matplotlib.pyplot as plt

def visualize(points):
    colors = [0]
    for point in points:
        plt.scatter(point[0], point[1], c=colors,s=1)
    plt.show()


if __name__ == "__main__":
    controller = SwarmController(["radio://0/80/2M/E7E7E7E7E7"])
    controller.take_off_and_scan_around()
    controller.point_cloud.save()
    points = controller.point_cloud.get_points()
    # points = [
    #     [0,1,1],
    #     [1, 1, 1],
    #     [1, 0, 1],
    #     [0.5,0.5,1],
    #     [0,0,1],
    #
    # ]

    visualize(points)

