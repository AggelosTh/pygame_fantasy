import pygame
from entities import TiledMap, Player, screen

# Initialize Pygame
pygame.init()
pygame.mixer.init()
clock = pygame.time.Clock()

tmx_map = TiledMap("map/test_map.tmx")
player_img = 'geralt.bmp'
player = Player(player_img, 20, 20)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
while running:
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Update
    all_sprites.update(keys)

    # Draw / r ender
    screen.fill((0, 0, 0))
    tmx_map.make_map(screen)
    all_sprites.draw(screen)

    # After draw everything, flip the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
