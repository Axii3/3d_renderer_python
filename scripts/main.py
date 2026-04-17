import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
deltatime = 0.0
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#FFD543")


    pygame.display.flip()

    deltatime = clock.tick(60) / 1000

pygame.quit()
