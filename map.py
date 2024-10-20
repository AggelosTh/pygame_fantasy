import pygame
from entities import TiledMap, Player, screen

# Initialize Pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

tmx_map = TiledMap("map/test_map.tmx")
player = Player(20, 20)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    player.update(keys)

    screen.fill((0, 0, 0))

    tmx_map.make_map(screen)

    all_sprites.draw(screen)
    
    # Update the display
    pygame.display.flip()
    # pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
