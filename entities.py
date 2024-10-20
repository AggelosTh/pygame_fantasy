import pygame
import pytmx
from pygame.locals import *

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
                        # This block converts the map to isometric. If we want to disable it
                        # we need to comment the following code and uncomment the next one.
                        tile = tile.convert_alpha()
                        screen_x = (x - y) * (tilewidth // 2) + (screen_width // 2)
                        screen_y = (x + y) * (tileheight // 2)
                        surface.blit(tile, (screen_x, screen_y + 20))
                        # surface.blit(tile, (x * self.tmxdata.tilewidth,
                        #                     y * self.tmxdata.tileheight))

    def make_map(self, screen):
        # temp_surface = pygame.Surface((self.width, self.height))
        self.render(screen)
        # return temp_surface



class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y, map_width, map_height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file).convert_alpha()  # Load player sprite
        self.rect = self.image.get_rect()
        self.map_x = x
        self.map_y = y
        self.speed = 1

    def move(self, dx, dy):
        self.map_x += dx
        self.map_y += dy

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

        self.rect.x = (self.map_x - self.map_y) * (tilewidth // 2) + (tilewidth // 2) - self.image.get_width() // 2
        self.rect.y = (self.map_x + self.map_y) * (tileheight // 2) - self.image.get_height()
