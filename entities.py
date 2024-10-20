import pygame
import pytmx
from pygame.locals import *

width = 40
height = 30
tilewidth = 32
tileheight = 16


# screen_width = width * tilewidth
# screen_height = height * tileheight

# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.init()
class Screen:
    def __init__(self):
        pass

    def get_screen_size():
        info = pygame.display.Info()
        return (info.current_w, info.current_h)

# screen_width, screen_height = Screen.get_screen_size()

# # Set up the display with V-Sync
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.SRCALPHA)
# pygame.display.set_caption("2D Isometric Game")

class TiledMap:
    def __init__(self, screen_w, screen_h, filename: str):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        # self.width = tm.width * tm.tilewidth
        # self.height = tm.height * tm.tileheight
        self.tmxdata = tm
        self.screen_w = screen_w
        self.screen_h = screen_h


    def render(self, surface: pygame.Surface):
        # Calculate the center offsets
        center_x = self.screen_w // 2
        center_y = self.screen_h // 2

        for layer in self.tmxdata.visible_layers:
            if isinstance(layer, pytmx.TiledTileLayer):
                for x, y, gid, in layer:
                    tile = self.tmxdata.get_tile_image_by_gid(gid)
                    if tile:
                        # This block converts the map to ismetric. If we want to disable it
                        # we need to comment the following code and uncomment the next one.
                        tile = tile.convert_alpha()
                        # screen_x = (x - y) * (tilewidth // 2) + (self.screen_w // 2)
                        # screen_y = (x + y) * (tileheight // 2)
                        screen_x = (x - y) * (self.tmxdata.tilewidth // 2) + center_x
                        screen_y = (x + y) * (self.tmxdata.tileheight // 2) + center_y
                        surface.blit(tile, (screen_x, screen_y -100)) # It center the tilemap using the top right corner, so we need to subtract 
                        # surface.blit(tile, (x * self.tmxdata.tilewidth,
                        #                     y * self.tmxdata.tileheight))

    def make_map(self, screen):
        # temp_surface = pygame.Surface((self.width, self.height))
        self.render(screen)
        # return temp_surface



class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y):
        super().__init__()
        # self.image = pygame.image.load(image_file).convert_alpha()  # Load player sprite
        self.image = pygame.transform.scale(pygame.image.load(image_file).convert_alpha(), (tilewidth, tileheight))  # Load player sprite and rescale to the tile dimensions
        self.rect = self.image.get_rect()
        self.map_x = x
        self.map_y = y 
        self.speed = 1

        # Set initial position in isometric coordinates
        self.update_rect_position()

    def move(self, dx, dy):
        self.map_x += dx
        self.map_y += dy
        self.update_rect_position()

    def update_rect_position(self):
            # Update the rect position based on the map_x and map_y
            self.rect.x = (self.map_x - self.map_y) * (tilewidth // 2) + (tilewidth // 2) - self.image.get_width() // 2
            self.rect.y = (self.map_x + self.map_y) * (tileheight // 2) - self.image.get_height()

    def update(self, keys):
        dx = dy = 0
        if keys[K_LEFT]:
            dx = -self.speed
        if keys[K_RIGHT]:
            dx = self.speed
        if keys[K_UP]:
            dy = -self.speed
        if keys[K_DOWN]:
            dy = self.speed
        
        # Adjust movement for isometric map
        self.move(dx, dy)

        # self.rect.x = (self.map_x - self.map_y) * (tilewidth // 2) + (tilewidth // 2) - self.image.get_width() // 2
        # self.rect.y = (self.map_x + self.map_y) * (tileheight // 2) - self.image.get_height()
