import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))  # width and height
pygame.display.set_caption('Runner')

icon = pygame.image.load('./assets/runner_icon.jpeg')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

test_surface = pygame.Surface((100, 200))  # width and height
test_surface.fill('Red')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # block image transfer -> puts one surface on anothe surface
    screen.blit(test_surface, (0, 0))

    pygame.display.update()
    clock.tick(60)
