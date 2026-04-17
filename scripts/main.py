import pygame
from pygame import Vector2
import renderer
from renderer import Vertex
import window

### references

### variables

window.render.add_vertex(Vertex(Vector2(-50, 50)))
window.render.add_vertex(Vertex(Vector2(50, 50)))
window.render.add_vertex(Vertex(Vector2(50, -50)))
#window.render.add_vertex(Vertex(Vector2(-40, -50)))

while window.running:
    for event in window.pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False

    window.screen.fill("#000000")

    # draw
    window.render.draw_vertices()

    # update
    renderer.camera_position.x += 0.1

    window.pygame.display.flip()
    window.deltatime = window.clock.tick(60) / 1000


window.pygame.quit()
