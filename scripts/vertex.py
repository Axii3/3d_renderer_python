import pygame
import window

pygame.init()


class Vertex():
	def __init__(self, position):
		self.position = position
		pass
	def draw(self, screen):
		pygame.draw.circle(screen, "#FFFFFF", (window.width/2 + self.position.x, window.height/2 + self.position.y), 10.0)
