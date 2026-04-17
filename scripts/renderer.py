
import pygame
import pygame.gfxdraw
from pygame import Vector3
from pygame import Vector2

pygame.init()

### references

### variables
camera_position = Vector3(0, 0, 0)
window_width = 0
window_height = 0
field_of_view = 300
near_clipping_plane = -50
vertex_rendering = True

class Renderer():
	def __init__(self, screen):
		self.triangles = []
		self.vertices = []
		self.screen = screen

	def draw(self):
		for t in range(len(self.triangles)):
			current_triangle = self.triangles[t]
			current_triangle.draw(self.screen)
			

	def add_triangle(self, v1, v2, v3):
		self.triangles.append(Triangle(self.screen, self.vertices[v1], self.vertices[v2], self.vertices[v3]))

	def add_vertex(self, vertex):
		self.vertices.append(vertex)

class Vertex():
	def __init__(self, position):
		self.world_position = position
		pass
	def draw(self, screen):
		pos = self.get_screen_space_pos()
		pygame.draw.circle(screen, "#FFFFFF", (window_width/2 + pos.x, window_height/2 + pos.y), 5.0)

	def get_screen_space_pos(self):
		vs_pos = self.get_view_space_pos()
		if (vs_pos.z + field_of_view < 0):
			vs_pos.z = -field_of_view + 1
		ss_x = (vs_pos.x * field_of_view) / (vs_pos.z + field_of_view)
		ss_y = -(vs_pos.y * field_of_view) / (vs_pos.z + field_of_view)

		# offset pivot from top left to center
		ss_vector = Vector2(ss_x, ss_y)
		return ss_vector

	def get_view_space_pos(self):
		view_pos = Vector3(self.world_position.x - camera_position.x, self.world_position.y - camera_position.y, self.world_position.z - camera_position.z)
		return view_pos

	def on_screen(self):
		if (self.get_view_space_pos().z + field_of_view < near_clipping_plane):
			return False

		return True

class Triangle():
	def __init__(self, screen, vertex1, vertex2, vertex3):
		self.screen = screen
		self.vertex1 = vertex1
		self.vertex2 = vertex2
		self.vertex3 = vertex3

	def draw(self, screen):
		if not (self.vertex1.on_screen() or self.vertex2.on_screen() or self.vertex3.on_screen()):
			return


		col = (255, 255, 255)

		v1x = int(self.vertex1.get_screen_space_pos().x)
		v1y = int(self.vertex1.get_screen_space_pos().y)
		v2x = int(self.vertex2.get_screen_space_pos().x)
		v2y = int(self.vertex2.get_screen_space_pos().y)
		v3x = int(self.vertex3.get_screen_space_pos().x)
		v3y = int(self.vertex3.get_screen_space_pos().y)

		v3_width = abs(v2x - v3x)
		v3_height = abs(v2y - v3y)
		v3_m = v3_height / v3_width

		v2_width = abs(v1x - v3x)
		v2_height = abs(v1y - v3y)
		v2_m = v2_height / v2_width

		v1_width = abs(v2x - v1x)
		v1_height = abs(v2y - v1y)
		v1_m = v1_height / v1_width
		
		for x in range(v1_width):
			c_x = v1x + x
			c_y = int((x+1) * v1_m) - int(x * v2_m)

			for y in range(c_y):
				x_pixel_pos = int(window_width/2 + c_x)
				y_pixel_pos = int(window_height/2 + v1y) - y
				y_pixel_pos = y_pixel_pos - int(x * v2_m)
				pygame.gfxdraw.pixel(screen, x_pixel_pos, y_pixel_pos, col)
		
		for x_t2 in range(v2_width - v1_width):
			x =	x_t2 + v1_width
			c_x = v1x + x
			c_y = int((v3_width - (x_t2+1)) * v3_m) + int((v3_width-(x_t2+1)) * v2_m)
			#int((x + v1_width) * v2_m)

			for y in range(c_y):
				x_pixel_pos = int(window_width/2 + c_x)
				y_pixel_pos = int(window_height/2 + v1y) - y
				y_pixel_pos = y_pixel_pos - int(x * v2_m)
				pygame.gfxdraw.pixel(screen, x_pixel_pos, y_pixel_pos, col)
			


		#pygame.draw.line(self.screen, "#CCCCCC", self.vertex1.get_screen_space_pos(), self.vertex2.get_screen_space_pos(), 5)
		#pygame.draw.line(self.screen, "#CCCCCC", self.vertex2.get_screen_space_pos(), self.vertex3.get_screen_space_pos(), 5)
		#pygame.draw.line(self.screen, "#CCCCCC", self.vertex3.get_screen_space_pos(), self.vertex1.get_screen_space_pos(), 5)
		if vertex_rendering:
			self.vertex1.draw(screen)
			self.vertex2.draw(screen)
			self.vertex3.draw(screen)
