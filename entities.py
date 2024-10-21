import pygame
from map import TiledMap
from screen import Screen
from pygame.locals import *


# Initialize Pygame
pygame.init()
pygame.mixer.init()

# Set up the display with V-Sync
screen_width, screen_height = Screen.get_screen_size()
screen_center = (screen_width // 2, screen_height // 2)

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.SRCALPHA)
pygame.display.set_caption("2D Isometric Game")

clock = pygame.time.Clock()

filename_map = "map/test_map.tmx"

width = 40
height = 30
tilewidth = 32
tileheight = 16

tmx_map = TiledMap(screen_width, screen_height, filename_map)

map_width = tmx_map.width # number of tiles horizontally
map_height = tmx_map.height # number of tiles vertically

tilewidth = tmx_map.tilewidth
tileheight = tmx_map.tileheight

screen_x = (map_width + map_height) * (tilewidth // 2)
screen_y = (map_width + map_height) * (tileheight // 2)

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

        # self.rect.x = (self.map_x - self.map_y) * (tilewidth // 2) + (tilewidth // 2) - self.image.get_width() // 2
        # self.rect.y = (self.map_x + self.map_y) * (tileheight // 2) - self.image.get_height()
