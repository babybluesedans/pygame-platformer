import pygame as p
import sys

import player
import tile

class Game:
    def __init__(self):
        p.init()
        p.display.set_caption("unnamed platformer")
        self.screen = p.display.set_mode((1920, 1080))
        self.screen_r = self.screen.get_rect()
        self.clock = p.time.Clock()
        self.mr_fucks = player.Player()
        self.tile = tile.Tile(self.screen)
        self.dt = None

    
    def run(self):
        while True:
            self.process_events()

            self.update()

            self.render()            


    def process_events(self):
        self.dt = self.clock.tick(60) / 1000
        self.mr_fucks.move_processor(self.dt)
        for event in p.event.get():
                if event.type == p.QUIT:
                    p.quit()
                    sys.exit()

    def update(self):
        pass
    
    def render(self):
        self.screen.fill("black")
        self.mr_fucks.draw(self.screen)
        self.tile.render_line()

        p.display.update()
        p.display.flip()

Game().run()