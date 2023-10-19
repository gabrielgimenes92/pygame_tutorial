import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))  # width and height
pygame.display.set_caption('Runner')

icon = pygame.image.load('graphics/runner_icon.jpeg')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # block image transfer -> puts one surface on anothe surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))

    pygame.display.update()
    clock.tick(60)
