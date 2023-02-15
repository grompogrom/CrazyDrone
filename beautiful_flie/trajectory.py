URI1 = 'radio://0/80/2M/1'
URI2 = "radio://0/110/2M/E7E7E7E7E2"
URI3 = 'radio://0/80/2M/E7E7E7E7E7'
URI4 = "radio://0/80/2M/E7E7E7E7E8"
URI5 = 'radio://0/80/2M/E7E7E7E7E1'
URI6 = "radio://0/110/2M/E7E7E7E71B"

uris = {
	URI1,
	URI2,
	URI3,
	# URI4,
	# URI5,
	# URI6
}

point1 = [{'x': -1.5, 'y': 0.25, 'z': 0.5, 't': 2}]
point2 = [{'x': -1.5, 'y': -0.25, 'z': 0.5, 't': 2}]
point3 = [{'x': -1.5, 'y': 0.5, 'z': 0.5, 't': 2}]
point4 = [{'x': -1.5, 'y': -0.5, 'z': 1, 't': 2}]
point5 = [{'x': -1.5, 'y': 0.75, 'z': 1, 't': 2}]
point6 = [{'x': -1.5, 'y': -0.75, 'z': 1, 't': 2}]

takeoff_land = {
	URI1: point6,
	URI2: point4,
	URI3: point2,
	# URI4: point1,
	# URI5: point3,
	# URI6: point5
}