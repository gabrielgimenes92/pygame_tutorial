import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))  # width and height
pygame.display.set_caption('Runner')

icon = pygame.image.load('graphics/runner_icon.jpeg')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()
# font type, font size (none is the default)
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('graphics/Sky.png')
ground_surface = pygame.image.load('graphics/ground.png')
# test, Anti Aliasing[Bool], color
text_surface = test_font.render('My game', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png')
snail_x_pos = 600

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # block image transfer -> puts one surface on anothe surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_x_pos -= 4
    if snail_x_pos < -100:
        snail_x_pos = 810
    screen.blit(snail_surface, (snail_x_pos, 260))

    pygame.display.update()
    clock.tick(60)
