import pygame

class Screen:
    def __init__(self):
        pass

    def get_screen_size():
        info = pygame.display.Info()
        return (info.current_w, info.current_h)
    
pygame.init()
pygame.mixer.init()

screen_width, screen_height = Screen.get_screen_size()
screen_center = (screen_width // 2, screen_height // 2)
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN | pygame.SRCALPHA)

pygame.display.set_caption("2D Isometric Game")