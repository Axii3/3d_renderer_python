
import pygame
import renderer

pygame.init()

### refferences
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
render = renderer.Renderer(screen)

### variables
deltatime = 0.0
running = True
width = pygame.display.get_window_size()[0]
height = pygame.display.get_window_size()[1]



