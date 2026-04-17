
import pygame
import vertex

pygame.init()


class Renderer():
	def __init__(self, screen):
		self.vertices = []
		self.screen = screen

	def draw_vertices(self):
		for v in range(len(self.vertices)):
			self.vertices[v].draw(self.screen)

	def add_vertex(self, vertex):
		self.vertices.append(vertex)