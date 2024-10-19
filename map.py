import pygame
import pytmx

# Initialize Pygame
pygame.init()

width = 40
height = 30
tilewidth = 32
tileheight = 16

screen_width = width * tilewidth
screen_height = height * tileheight
screen = pygame.display.set_mode((screen_width, screen_height))


class TiledMap:
    def __init__(self, filename: str):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width * tm.tilewidth
        self.height = tm.height * tm.tileheight
        self.tmxdata = tm

    def render(self, surface: pygame.Surface):
        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        # This block converts the map to ismetric. If we want to disable it
                        # we need to comment the following code and uncomment the next one.
                        tile = tile.convert_alpha()
                        screen_x = (x - y) * (tilewidth // 2) + (screen_width // 2)
                        screen_y = (x + y) * (tileheight // 2)
                        surface.blit(tile, (screen_x, screen_y + 20))
                        # surface.blit(tile, (x * self.tmxdata.tilewidth,
                        #                     y * self.tmxdata.tileheight))

    def make_map(self):
        # temp_surface = pygame.Surface((self.width, self.height))
        self.render(screen)
        # return temp_surface
    

tmx_map = TiledMap("map/test_map.tmx")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the map
    tmx_map.make_map()

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
