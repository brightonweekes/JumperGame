import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
        self.rect = self.image.get_rect(bottomleft = (80, 300))
        self.y_vel = 0

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom == 300:
            self.y_vel = -20

    def jump(self):
        if self.y_vel != 0 or self.rect.bottom < 300:
            self.rect.y += self.y_vel
            self.y_vel += 1
        if self.rect.bottom > 300:
            self.rect.bottom = 300
            self.y_vel = 0

    def collision(self):
        if self.rect.colliderect(snail_rect):
            global game_active
            game_active = False

    def update(self):
        self.player_input()
        self.jump()
        self.collision()


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

player = pygame.sprite.GroupSingle()
player.add(Player())

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.bottom == 300 and player.rect.collidepoint(event.pos):
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

  
        player.draw(screen) 
        player.update()



    else:

        screen.fill('yellow')

        continue_tooltip = test_font.render('Press SPACE to continue...', False, 'Black')
        continue_tooltip.blit(screen, (0, 0,))


    pygame.display.update()
    clock.tick(fps)
