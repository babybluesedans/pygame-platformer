import pygame as p

class Tile:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = self.screen_rect.width // 40
        self.size = p.Vector2(self.width, self.width)
        self.img = p.transform.scale(p.image.load("platformer/Tile1.png"), (self.width, self.width))
        self.img_r = self.img.get_rect()

    def render_line(self):
        tiles_per_screen = self.screen_rect.width // self.width
        y = 700
        x = 0
        for i in range(tiles_per_screen):
            self.screen.blit(self.img, (x, y))
            print(x)
            x += self.width
        