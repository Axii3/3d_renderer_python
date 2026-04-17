
import pygame
from pygame import Vector3
from pygame import Vector2

pygame.init()

### references

### variables
camera_position = Vector3(0, 0, 1)
window_width = 0
window_height = 0
field_of_view = 150


class Renderer():
	def __init__(self, screen):
		self.vertices = []
		self.screen = screen

	def draw_vertices(self):
		for v in range(len(self.vertices)):
			current_vertex = self.vertices[v]
			current_vertex.draw(self.screen)
			#if (v>0):
			pygame.draw.line(self.screen, "#CCCCCC", current_vertex.get_screen_space_pos(), self.vertices[v-1].get_screen_space_pos(), 5)


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
		ss_x = (vs_pos.x * field_of_view) / (vs_pos.z + field_of_view)
		ss_y = (vs_pos.y * field_of_view) / (vs_pos.z + field_of_view)
		# offset pivot from top left to center
		offset_pos = Vector2(window_width/2 + ss_x, window_height/2 + ss_y)
		return offset_pos

	def get_view_space_pos(self):
		view_pos = Vector3(self.world_position.x - camera_position.x, self.world_position.y - camera_position.y, self.world_position.z - camera_position.z)
		return view_pos