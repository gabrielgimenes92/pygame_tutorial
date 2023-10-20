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

# convert image to a format easier for pygame
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
# test, Anti Aliasing[Bool], color
text_surface = test_font.render('My game', False, 'Black')

# with convert_alpha deletes the alpha values
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print("collision")

    # block image transfer -> puts one surface on anothe surface
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.x -= 4
    if snail_rect.right < 0:
        snail_rect.left = 800

    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    # if player_rect.colliderect(snail_rect):
    #     print("fudge")

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint(mouse_pos):
    #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
