import pygame
from pygame import Vector3
import renderer
from renderer import Vertex
import window

### references

# --

### variables
player_pos = Vector3(0, 0, 1)
player_speed = 100.0


window.render.add_vertex(Vertex(Vector3(-50, 50, 0)))
window.render.add_vertex(Vertex(Vector3(50, 50, 0)))
window.render.add_vertex(Vertex(Vector3(50, -50, 0)))
window.render.add_vertex(Vertex(Vector3(-50, -50, 0)))
window.render.add_vertex(Vertex(Vector3(-50, 50, 50)))
window.render.add_vertex(Vertex(Vector3(50, 50, 50)))
window.render.add_vertex(Vertex(Vector3(50, -50, 50)))
window.render.add_vertex(Vertex(Vector3(-50, -50, 50)))

while window.running:
    window.deltatime = window.clock.tick(60) / 1000
    deltatime = window.deltatime

    for event in window.pygame.event.get():
        if event.type == pygame.QUIT:
            window.running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.z += player_speed * deltatime
    if keys[pygame.K_s]:
        player_pos.z -= player_speed * deltatime
    if keys[pygame.K_a]:
        player_pos.x -= player_speed * deltatime
    if keys[pygame.K_d]:
        player_pos.x += player_speed * deltatime
    if keys[pygame.K_e]:
        renderer.field_of_view += 1
        print(renderer.field_of_view)


    window.screen.fill("#000000")

    # draw
    window.render.draw_vertices()

    # update
    renderer.camera_position.x = player_pos.x
    renderer.camera_position.y = player_pos.y
    renderer.camera_position.z = player_pos.z

    window.pygame.display.flip()



window.pygame.quit()
