
import pygame
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
vertex_rendering = False

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
		pygame.draw.circle(screen, "#FFFFFF", (pos.x, pos.y), 5.0)

	def get_screen_space_pos(self):
		vs_pos = self.get_view_space_pos()
		if (vs_pos.z + field_of_view < 0):
			vs_pos.z = -field_of_view + 1
		ss_x = (vs_pos.x * field_of_view) / (vs_pos.z + field_of_view)
		ss_y = -(vs_pos.y * field_of_view) / (vs_pos.z + field_of_view)

		# offset pivot from top left to center
		offset_pos = Vector2(window_width/2 + ss_x, window_height/2 + ss_y)
		return offset_pos

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

		pygame.draw.line(self.screen, "#CCCCCC", self.vertex1.get_screen_space_pos(), self.vertex2.get_screen_space_pos(), 5)
		pygame.draw.line(self.screen, "#CCCCCC", self.vertex2.get_screen_space_pos(), self.vertex3.get_screen_space_pos(), 5)
		pygame.draw.line(self.screen, "#CCCCCC", self.vertex3.get_screen_space_pos(), self.vertex1.get_screen_space_pos(), 5)
		if vertex_rendering:
			self.vertex1.draw(screen)
			self.vertex2.draw(screen)
			self.vertex3.draw(screen)
