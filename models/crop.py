transparent = 2
is_cube = False
glass = False
translucent = False

colliders = []

vertex_positions = [
	[ 0.25,  0.4375,  0.50,   0.25, -0.5625,  0.50,   0.25, -0.5625, -0.50,   0.25,  0.4375, -0.50], # right
	[ 0.25,  0.4375, -0.50,   0.25, -0.5625, -0.50,   0.25, -0.5625,  0.50,   0.25,  0.4375,  0.50], # right
	[-0.25,  0.4375, -0.50,  -0.25, -0.5625, -0.50,  -0.25, -0.5625,  0.50,  -0.25,  0.4375,  0.50], # left
	[-0.25,  0.4375,  0.50,  -0.25, -0.5625,  0.50,  -0.25, -0.5625, -0.50,  -0.25,  0.4375, -0.50], # left
	[-0.50,  0.4375,  0.25,  -0.50, -0.5625,  0.25,   0.50, -0.5625,  0.25,   0.50,  0.4375,  0.25], # front
	[ 0.50,  0.4375,  0.25,   0.50, -0.5625,  0.25,  -0.50, -0.5625,  0.25,  -0.50,  0.4375,  0.25], # front
	[ 0.50,  0.4375, -0.25,   0.50, -0.5625, -0.25,  -0.50, -0.5625, -0.25,  -0.50,  0.4375, -0.25], # back
	[-0.50,  0.4375, -0.25,  -0.50, -0.5625, -0.25,   0.50, -0.5625, -0.25,   0.50,  0.4375, -0.25], # back
]

tex_coords = [
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
	[0.0, 1.0, 0.0,  0.0, 0.0, 0.0,  1.0, 0.0, 0.0,  1.0, 1.0, 0.0],
]

shading_values = [
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[0.6, 0.6, 0.6, 0.6],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
	[0.8, 0.8, 0.8, 0.8],
]