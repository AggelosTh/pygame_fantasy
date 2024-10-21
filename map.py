import pygame
import pytmx
    
class TiledMap:
    def __init__(self, screen_w, screen_h, filename: str):
        tm = pytmx.load_pygame(filename, pixelalpha=True)
        self.width = tm.width
        self.height = tm.height
        self.tilewidth = tm.tilewidth
        self.tileheight = tm.tileheight
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
                        # This block converts the map to isometric. If we want to disable it
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


