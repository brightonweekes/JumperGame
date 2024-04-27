import pygame

pygame.init()

width, height = 800, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky = pygame.image.load('graphics/Sky.png')
ground = pygame.image.load('graphics/ground.png')

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(sky, (0, 0))
    screen.blit(ground, (0, 300))

    pygame.display.update()
    clock.tick(60)