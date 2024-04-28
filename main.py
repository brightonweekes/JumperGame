import pygame

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jumper')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
fps = 60

sky_surface = pygame.image.load('graphics/Sky.png').convert_alpha()
ground_surface = pygame.image.load('graphics/ground.png').convert_alpha()

score_surface = test_font.render('My Game', False, 'black').convert_alpha()
score_rect = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomleft = (800, 300))
snail_x_vel = -4 * 60/fps

player_surface = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(bottomleft = (80, 300))


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            if player_rect.collidepoint(event.pos):
                print('mouse is over player')
        if event.type == pygame.MOUSEBUTTONDOWN:
            print('mouse down')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'pink', score_rect)
    pygame.draw.ellipse(screen, 'Black', pygame.Rect(50, 200, 100, 100), 10)
    screen.blit(score_surface, score_rect)

    snail_rect.x += snail_x_vel
    if snail_rect.right <= 0:     snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    player_rect.colliderect(snail_rect)

    pygame.display.update()
    clock.tick(fps)