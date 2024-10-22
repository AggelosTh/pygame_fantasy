import pygame
from pytmx.util_pygame import load_pygame
from screen import screen_width, screen_height

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

class TiledMap:
    def __init__(self, map_file, sprite_group):
        self.tmx_data = load_pygame(map_file)
        self.sprite_group = sprite_group
        self.center_x = screen_width // 2
        self.center_y = screen_height // 2

    def load_tiles(self):
        for layer in self.tmx_data.visible_layers:
            if hasattr(layer, 'data'):
                for x, y, surf in layer.tiles():
                    iso_x = (x - y) * (self.tmx_data.tilewidth // 2) + self.center_x
                    iso_y = (x + y) * (self.tmx_data.tileheight // 2) + self.center_y
                    pos = (iso_x, iso_y - 100)
                    Tile(pos=pos, surf=surf, groups=self.sprite_group)

    def draw(self, surface):
        self.sprite_group.draw(surface)

# # Usage
# pygame.init()
# sprite_group = pygame.sprite.Group()
# tiled_map = TiledMap('map/test_map.tmx', sprite_group)
# tiled_map.load_tiles()

# # Main game loop
# while True:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()

#     screen.fill((0, 0, 0))  # Clear the screen
#     tiled_map.draw(screen)  # Draw the tiles

#     pygame.display.update()  # Update the display
