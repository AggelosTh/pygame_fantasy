import sys
import pygame
from entities import Player, screen, screen_x, screen_y, screen_center, tmx_map, clock

###### Helper functions ######


###### Main Code ######

player_img = 'sad_sprite.png' # Added new sprite because it has clear background and is round so it displays better with new dims
player = Player(player_img, screen_x, screen_y)

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Game loop
running = True
game_over = False
paused = False

while running:
    # Process input (events)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if game_over:
                    pygame.quit()
                    sys.exit()
            if event.key == pygame.K_p:
                if paused:
                    # Unpause the game and set the game_over back to False
                    paused = False
                    game_over = False
                else:
                    # Pause the game
                    paused = True
                    
    
    if not game_over:
        if not paused:
            keys = pygame.key.get_pressed()
            player.update(keys)

            screen.fill((0, 0, 0))

            tmx_map.make_map(screen)

            all_sprites.draw(screen)

        if paused:
            # Draw a pause overlay or message here
            font = pygame.font.Font(None, 74)
            text = font.render("Paused", True, (255, 255, 255))
            screen.blit(text, text.get_rect(center=screen_center))
            game_over = True # Set the game over to true in case you want to exit the game pressing ESC

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit Pygame
pygame.quit()
