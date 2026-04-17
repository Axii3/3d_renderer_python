import pygame
from pygame import Vector2
from vertex import Vertex
import renderer
import window

### references

### variables

window.render.add_vertex(Vertex(Vector2(-50, 0)))
window.render.add_vertex(Vertex(Vector2(50, 0)))

while window.running:
    for event in window.pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False

    window.screen.fill("#000000")

    # draw
    window.render.draw_vertices()


    window.pygame.display.flip()
    window.deltatime = window.clock.tick(60) / 1000


window.pygame.quit()
