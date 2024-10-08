import pygame as p
import math

class Tile:
    def __init__(self, screen, x=0, y=0,):
        self.screen = screen
        self.x = x
        self.y = y
        self.screen_rect = screen.get_rect()
        self.width = self.screen_rect.width // 40
        self.height = self.width
        self.size = p.Vector2(self.height, self.width)
        self.img = p.transform.scale(p.image.load("platformer/Tile1.png"), (self.height, self.width))
        self.img_r = self.img.get_rect()
        self.rect = p.Rect(x, y, self.width, self.height)
    