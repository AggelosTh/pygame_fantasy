import pygame
from alt_map import TiledMap
from pygame.locals import *

clock = pygame.time.Clock()

filename_map = "map/test_map.tmx"

width = 40
height = 30
tilewidth = 32
tileheight = 16

sprite_group = pygame.sprite.Group()

tmx_map = TiledMap(filename_map, sprite_group)

class Player(pygame.sprite.Sprite):
    def __init__(self, image_file, x, y):
        super().__init__()
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
