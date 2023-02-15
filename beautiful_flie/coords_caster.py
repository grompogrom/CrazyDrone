class CoordsCaster():
	def __init__(self, area_xy, area_length, area_width):
		self.center = list(map(lambda x: x/2, area_xy))
		self.min_x = area_xy[0] / 2 - area_length / 2
		self.min_y = area_xy[1] / 2 - area_width / 2

	def cast_coords(self, x, y, z):
		new_x = self.center[0] + x
		new_y = self.center[1] + y
		new_z = z
		return new_x, new_y, new_z


if __name__ == '__main__':
	c = CoorsCaster([5,5], 4,4)
	print(c.cast_coords(1,2,3))