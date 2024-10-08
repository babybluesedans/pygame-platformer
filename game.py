import pygame as p
import sys

import player
import tile
import test_level

class Game:
    def __init__(self):
        p.init()
        p.display.set_caption("unnamed platformer")
        self.screen = p.display.set_mode((1920, 1104))
        self.screen_r = self.screen.get_rect()
        self.clock = p.time.Clock()
        self.tile = tile.Tile(self.screen)
        self.level = test_level.Level(self.screen)
        self.mr_fucks = player.Player(self.level)

    
    def run(self):
        while True:
            self.process_events()

            self.update()

            self.render()            


    def process_events(self):
        self.dt = self.clock.tick(60) / 1000
        for event in p.event.get():
            self.mr_fucks.event_processor(event)
            if event.type == p.QUIT:
                p.quit()
                sys.exit()

        self.mr_fucks.move_processor()

    def update(self):
        pass
    
    def render(self):
        self.screen.fill("black")
        self.mr_fucks.draw(self.screen)
        self.level.draw_tilemap()

        p.display.update()
        p.display.flip()

Game().run()