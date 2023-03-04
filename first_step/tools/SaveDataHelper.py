def save_points_to_file(points):
    data = ""
    for point in points:
        data += f"x={point[0]}   y={point[1]}\n"
    with open("PointCloudRes.txt", 'w') as f:
        f.write(data)
