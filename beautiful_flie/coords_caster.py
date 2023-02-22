class CoordsCaster():
	def __init__(self, area_xy, area_length, area_width):
		self.center = list(map(lambda x: x/2, area_xy))
		self.max_x = area_length / 2
		self.max_y = area_width / 2

	def cast_coords(self, x, y, z):
		# assert self.max_x > abs(x)
		# assert self.max_y > abs(y)
		new_x = self.center[0] + x
		new_y = self.center[1] + y
		new_z = z
		return new_x, new_y, new_z


if __name__ == '__main__':
	c = CoordsCaster([5,5], 4,4)
	print(c.cast_coords(1,2,3))