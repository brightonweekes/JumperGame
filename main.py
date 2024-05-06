import pygame

pygame.init()

game_active = True
width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jumper')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
fps = 60
snail_x_vel = -4

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = test_font.render('My Game', False, 'black').convert_alpha()
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80, 300))
player_y_vel = 0


running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.bottom == 300 and player_rect.collidepoint(event.pos):
                    player_y_vel = -20
        else:
            if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        game_active = True
                        snail_rect.left = 800
                
    if game_active:
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, 300))
        screen.blit(score_surface, score_rect)

        snail_rect.x += snail_x_vel
        if snail_rect.right <= 0:     
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and player_rect.bottom == 300:
            player_y_vel = -20

        if player_y_vel != 0 or player_rect.bottom < 300:
            player_rect.y += player_y_vel
            player_y_vel += 1
        if player_rect.bottom > 300:
            player_rect.bottom = 300
            player_y_vel = 0


        screen.blit(player_surface, player_rect)   


        if player_rect.colliderect(snail_rect):
            game_active = False
    else:

        screen.fill('yellow')

        continue_tooltip = test_font.render('Press SPACE to continue...', False, 'Black')
        continue_tooltip.blit(screen, (0, 0,))


    pygame.display.update()
    clock.tick(fps)
