
URI1 = 'radio://0/80/2M/1'
URI2 = "radio://0/80/2M/E7E7E7E7E2"
URI3 = 'radio://0/80/2M/E7E7E7E7E7'
URI4 = "radio://0/80/2M/E7E7E7E7E8"
URI5 = 'radio://0/80/2M/E7E7E7E7E1'
# URI1 = "radio://0/110/2M/E7E7E7E71B"
URI6 = ""

uris = {
    URI1,
    URI2,
    URI3,
    # URI4,
    # URI5,
    # URI6
}

# Start position
point1 = [{'x': -1.5, 'y': 0.30, 'z': 0.5, 't': 2}]
point2 = [{'x': -1.5, 'y': -0.30, 'z': 0.5, 't': 2}]
point3 = [{'x': -1.5, 'y': 0.6, 'z': 0.5, 't': 2}]
point4 = [{'x': -1.5, 'y': -0.6, 'z': 1, 't': 2}]
point5 = [{'x': -1.5, 'y': 1, 'z': 1, 't': 2}]
point6 = [{'x': -1.5, 'y': -1, 'z': 1, 't': 2}]

# Start triangle position
pointA = [{'x': 0.27, 'y': 0.45, 'z': 0.5, 't': 2}]
pointB = [{'x': 0.27, 'y': -0.45, 'z': 0.5, 't': 2}]
pointC = [{'x': -0.51, 'y': 0, 'z': 0.5, 't': 2}]

pointA_1 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]
pointB_1 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
pointC_1 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]

# First swap points in little triangle  and big triangles
s_pointl_1 = [{'x': 0.27, 'y': -0.45, 'z': 0.5, 't': 2}]
s_pointl2_1 = [{'x': -0.51, 'y': 0, 'z': 0.5, 't': 2}]
s_pointl3_1 = [{'x': 0.27, 'y': 0.45, 'z': 0.5, 't': 2}]

s_pointb_1 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]
s_pointb2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s_pointb3_1 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]

# Second swap points in little triangle  and big triangles
s_pointl_2 = [{'x': -0.51, 'y': 0, 'z': 0.5, 't': 2}]
s_pointl2_2 = [{'x': 0.27, 'y': 0.45, 'z': 0.5, 't': 2}]
s_pointl3_2 = [{'x': 0.27, 'y': -0.45, 'z': 0.5, 't': 2}]

s_pointb_2 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s_pointb2_2 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]
s_pointb3_2 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]

# Third swap points in little triangle  and big triangles
s_pointl_3 = [{'x': 0.27, 'y': 0.45, 'z': 0.5, 't': 2}]
s_pointl2_3 = [{'x': 0.27, 'y': -0.45, 'z': 0.5, 't': 2}]
s_pointl3_3 = [{'x': -0.51, 'y': 0, 'z': 0.5, 't': 2}]

s_pointb_3 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]
s_pointb2_3 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s_pointb3_3 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]

# Swap height little triangle to height big triangle
sh_pointl_1 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
sh_pointl2_1 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
sh_pointl3_1 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]

sh_pointb_1 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]
sh_pointb2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
sh_pointb3_1 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]

# First swap2 points in little triangle  and big triangles at new height
s2_pointl_1 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
s2_pointl2_1 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]
s2_pointl3_1 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]

s2_pointb_1 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]
s2_pointb2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s2_pointb3_1 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]

# Second swap2 points in little triangle  and big triangles at new height
s2_pointl_2 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]
s2_pointl2_2 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
s2_pointl3_2 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]

s2_pointb_2 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s2_pointb2_2 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]
s2_pointb3_2 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]

# Third swap2 points in little triangle  and big triangles at new height
s2_pointl_3 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
s2_pointl2_3 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
s2_pointl3_3 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]

s2_pointb_3 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]
s2_pointb2_3 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
s2_pointb3_3 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]

# Swap height big triangle
sh2_pointl_1 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
sh2_pointl2_1 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
sh2_pointl3_1 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]

sh2_pointb_1 = [{'x': -0.66, 'y': 1.17, 'z': 1.5, 't': 2}]
sh2_pointb2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1.5, 't': 2}]
sh2_pointb3_1 = [{'x': 1.2, 'y': 0, 'z': 1.5, 't': 2}]

# First swap2 points in little triangle  and big triangles at new height
s3_pointl_1 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
s3_pointl2_1 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]
s3_pointl3_1 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]

s3_pointb_1 = [{'x': 1.2, 'y': 0, 'z': 1.5, 't': 2}]
s3_pointb2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1.5, 't': 2}]
s3_pointb3_1 = [{'x': -0.66, 'y': 1.17, 'z': 1.5, 't': 2}]

# Second swap2 points in little triangle  and big triangles at new height
s3_pointl_2 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]
s3_pointl2_2 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
s3_pointl3_2 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]

s3_pointb_2 = [{'x': -0.66, 'y': -1.17, 'z': 1.5, 't': 2}]
s3_pointb2_2 = [{'x': 1.2, 'y': 0, 'z': 1.5, 't': 2}]
s3_pointb3_2 = [{'x': -0.66, 'y': -1.17, 'z': 1.5, 't': 2}]

# Third swap2 points in little triangle  and big triangles at new height
s3_pointl_3 = [{'x': 0.27, 'y': 0.45, 'z': 1, 't': 2}]
s3_pointl2_3 = [{'x': 0.27, 'y': -0.45, 'z': 1, 't': 2}]
s3_pointl3_3 = [{'x': -0.51, 'y': 0, 'z': 1, 't': 2}]

s3_pointb_3 = [{'x': -0.66, 'y': 1.17, 'z': 1.5, 't': 2}]
s3_pointb2_3 = [{'x': -0.66, 'y': -1.17, 'z': 1.5, 't': 2}]
s3_pointb3_3 = [{'x': 1.2, 'y': 0, 'z': 1.5, 't': 2}]

# Swap scales little and big triangles

ss_pointl_1 = [{'x': -0.66, 'y': 1.17, 'z': 1, 't': 2}]
ss_pointl2_1 = [{'x': -0.66, 'y': -1.17, 'z': 1, 't': 2}]
ss_pointl3_1 = [{'x': 1.2, 'y': 0, 'z': 1, 't': 2}]

ss_pointb_1 = [{'x': 0.27, 'y': 0.45, 'z': 1.5, 't': 2}]
ss_pointb2_1 = [{'x': 0.27, 'y': -0.45, 'z': 1.5, 't': 2}]
ss_pointb3_1 = [{'x': -0.51, 'y': 0, 'z': 1.5, 't': 2}]

# Land drones
sl_pointl_1 = [{'x': -0.66, 'y': 1.17, 'z': 0, 't': 2}]
sl_pointl2_1 = [{'x': -0.66, 'y': -1.17, 'z': 0, 't': 2}]
sl_pointl3_1 = [{'x': 1.2, 'y': 0, 'z': 0, 't': 2}]

sl_pointb_1 = [{'x': 0.27, 'y': 0.45, 'z': 0, 't': 2}]
sl_pointb2_1 = [{'x': 0.27, 'y': -0.45, 'z': 0, 't': 2}]
sl_pointb3_1 = [{'x': -0.51, 'y': 0, 'z': 0, 't': 2}]


takeoff_land = {
    URI1: point6,
    URI2: point4,
    URI3: point2,
    URI4: point1,
    URI5: point3,
    URI6: point5
}

figure_1 = {
	URI1: pointA_1,
	URI2: pointB_1,
	URI3: pointC_1,
	URI4: pointA,
	URI5: pointB,
	URI6: pointC
}

figure_2 = {
	URI1: pointC_1,
	URI2: pointA_1,
	URI3: pointB_1,
	URI4: pointA,
	URI5: pointB,
	URI6: pointB
}

figure_3 = {
	URI1: pointB_1,
	URI2: pointC_1,
	URI3: pointA_1,
	URI4: pointA,
	URI5: pointB,
	URI6: pointB
}
