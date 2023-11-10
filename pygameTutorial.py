import pygame
from sys import exit

game_active = True

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
score_surf = test_font.render('My game', False, (64, 64, 64))
score_rect = score_surf.get_rect(center=(400, 50))

# with convert_alpha deletes the alpha values
snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(600, 300))

player_surf = pygame.image.load(
    'graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN and player_rect.bottom >= 300:
                if player_rect.collidepoint(event.pos):
                    player_gravity = -20
            if event.type == pygame.KEYDOWN and player_rect.bottom >= 300:
                if event.key == pygame.K_SPACE:
                    player_gravity = -20
        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                snail_rect.left = 600
                game_active = True

    if game_active:
        # block image transfer -> puts one surface on anothe surface
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        pygame.draw.rect(screen, '#c0e8ec', score_rect)
        pygame.draw.rect(screen, '#c0e8ec', score_rect, 10)
        # pygame.draw.line(screen, 'Black', (0, 0), pygame.mouse.get_pos())
        # pygame.draw.ellipse(screen, 'Brown', pygame.Rect(50, 200, 100, 100))
        screen.blit(score_surf, score_rect)

        snail_rect.x -= 4
        if snail_rect.right < 0:
            snail_rect.left = 800
        screen.blit(snail_surf, snail_rect)

        # Player
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Collision
        if snail_rect.colliderect(player_rect):
            game_active = False

    else:
        screen.fill("Yellow")

       # keys = pygame.key.get_pressed()
       # if keys[pygame.K_SPACE]:
       #     print('jump')

       # if player_rect.colliderect(snail_rect):
       #     print("fudge")

       # mouse_pos = pygame.mouse.get_pos()
       # if player_rect.collidepoint(mouse_pos):
       #     print(pygame.mouse.get_pressed())

    pygame.display.update()
    clock.tick(60)
