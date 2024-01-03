import math
import entity
import glm
import options
import chunk

WALKING_SPEED = 4.317
SPRINTING_SPEED = 7 # faster than in Minecraft, feels better

class Frustum:
	left = glm.vec4(1.0)
	right = glm.vec4(1.0)
	top = glm.vec4(1.0)
	bottom = glm.vec4(1.0)
	near = glm.vec4(1.0)
	far = glm.vec4(1.0)

def normalize(plane):
	return plane / glm.length(plane.xyz)


class Player(entity.Entity):
	def __init__(self, world, shader, width, height):
		super().__init__(world)

		self.view_width = width
		self.view_height = height

		# create matrices

		self.mv_matrix = glm.mat4()
		self.p_matrix = glm.mat4()

		# shaders

		self.shader = shader

		self.mvp_matrix_location = self.shader.find_uniform(b"u_MVPMatrix")
		

		# camera variables

		self.eyelevel = self.height - 0.2
		self.input = [0, 0, 0]

		self.target_speed = WALKING_SPEED
		self.speed = self.target_speed

		self.interpolated_position = self.position
		self.rounded_position = self.position
		self.view_ray = glm.vec3(1.0)

	def update(self, delta_time):
		# process input

		self.view_ray = glm.vec3(glm.cos(self.rotation[0]) * glm.cos(self.rotation[1]), 
						glm.sin(self.rotation[1]),
						glm.sin(self.rotation[0]) * glm.cos(self.rotation[1]))

		if delta_time * 20 > 1:
			self.speed = self.target_speed

		else:
			self.speed += (self.target_speed - self.speed) * delta_time * 20

		multiplier = self.speed * (1, 2)[self.flying]

		if self.flying and self.input[1]:
			self.accel[1] = self.input[1] * multiplier

		if self.input[0] or self.input[2]:
			angle = self.rotation[0] - math.atan2(self.input[2], self.input[0]) + math.tau / 4

			self.accel[0] = math.cos(angle) * multiplier
			self.accel[2] = math.sin(angle) * multiplier

		if not self.flying and self.input[1] > 0:
			self.jump()

		# process physics & collisions &c

		super().update(delta_time)

		self.rounded_position = [round(i) for i in self.position]
	
	def update_interpolation(self, delta_time):
		self.interpolated_position = glm.mix(glm.vec3(self.position), glm.vec3(self.old_position), self.step)
		self.step -= delta_time

	def update_frustum(self, mat):
		mat = glm.transpose(mat)
		for i in range(4): 
			Frustum.left[i]      = mat[3][i] + mat[0][i]
			Frustum.right[i]     = mat[3][i] - mat[0][i]
			Frustum.bottom[i]    = mat[3][i] + mat[1][i]
			Frustum.top[i]       = mat[3][i] - mat[1][i]
			Frustum.near[i]      = mat[3][i] + mat[2][i]
			Frustum.far[i]       = mat[3][i] - mat[2][i]
			
		Frustum.left = normalize(Frustum.left)
		Frustum.right = normalize(Frustum.right)
		Frustum.bottom = normalize(Frustum.bottom)
		Frustum.top = normalize(Frustum.top)
		Frustum.near = normalize(Frustum.near)
		Frustum.far = normalize(Frustum.far)
		
	def check_in_frustum(self, chunk_pos):
		"""Frustum check of each chunk. If the chunk is not in the view frustum, it is discarded"""
		planes = (Frustum.left, Frustum.right, Frustum.bottom, Frustum.top, Frustum.near, Frustum.far)
		result = 2
		center = glm.vec3(chunk_pos * glm.ivec3(chunk.CHUNK_WIDTH, 0, chunk.CHUNK_LENGTH)
									+ glm.ivec3(chunk.CHUNK_WIDTH / 2, 
												chunk.CHUNK_HEIGHT / 2,
												chunk.CHUNK_LENGTH / 2))


		for plane in planes:
			_in = 0
			_out = 0
			normal = plane.xyz
			w = plane.w
			if glm.dot(normal, center + glm.vec3(chunk.CHUNK_WIDTH / 2, chunk.CHUNK_HEIGHT / 2, chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(-chunk.CHUNK_WIDTH / 2, chunk.CHUNK_HEIGHT / 2, chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(chunk.CHUNK_WIDTH / 2, chunk.CHUNK_HEIGHT / 2, -chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(-chunk.CHUNK_WIDTH / 2, chunk.CHUNK_HEIGHT / 2, -chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(chunk.CHUNK_WIDTH / 2, -chunk.CHUNK_HEIGHT / 2, chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(-chunk.CHUNK_WIDTH / 2, -chunk.CHUNK_HEIGHT / 2, chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(chunk.CHUNK_WIDTH / 2, -chunk.CHUNK_HEIGHT / 2, -chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			if glm.dot(normal, center + glm.vec3(-chunk.CHUNK_WIDTH / 2, -chunk.CHUNK_HEIGHT / 2, -chunk.CHUNK_LENGTH / 2)) + w < 0:
				_out += 1
			else:
				_in += 1
			
			if not _in:
				return 0
			elif _out:
				result = 1
		return result

	def update_matrices(self):
		# create projection matrix
		
		self.p_matrix = glm.perspective(
			glm.radians(options.FOV + 10 * (self.speed - WALKING_SPEED) / (SPRINTING_SPEED - WALKING_SPEED)),
			float(self.view_width) / self.view_height, 0.1, 500)

		# create modelview matrix

		self.mv_matrix = glm.mat4(1.0)
		self.mv_matrix = glm.rotate(self.mv_matrix, self.rotation[1], -glm.vec3(1.0, 0.0, 0.0))
		self.mv_matrix = glm.rotate(self.mv_matrix, self.rotation[0] + math.tau / 4, glm.vec3(0.0, 1.0, 0.0))

		self.mv_matrix = glm.translate(self.mv_matrix, -glm.vec3(*self.interpolated_position) - glm.vec3(0, self.eyelevel, 0))

		# modelviewprojection matrix

		self.shader.uniform_matrix(self.mvp_matrix_location, self.p_matrix * self.mv_matrix)
		self.update_frustum(self.p_matrix * self.mv_matrix)