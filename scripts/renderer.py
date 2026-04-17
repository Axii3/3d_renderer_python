
import pygame

pygame.init()

### references

### variables
camera_position = pygame.Vector2(0, 0)
window_width = 0
window_height = 0



class Renderer():
	def __init__(self, screen):
		self.vertices = []
		self.screen = screen

	def draw_vertices(self):
		for v in range(len(self.vertices)):
			current_vertex = self.vertices[v]
			current_vertex.draw(self.screen)
			pygame.draw.line(self.screen, "#CCCCCC", current_vertex.screen_position, self.vertices[v-1].screen_position, 5)

	def add_vertex(self, vertex):
		self.vertices.append(vertex)

class Vertex():
	def __init__(self, position):
		self.position = position
		self.screen_position = pygame.Vector2(window_width/2 + self.position.x, window_height/2 + self.position.y)
		pass
	def draw(self, screen):
		pygame.draw.circle(screen, "#FFFFFF", (self.screen_position.x, self.screen_position.y), 10.0)
