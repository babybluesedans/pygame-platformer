import pygame as p

class Player:
    def __init__(self):
        self.img = p.transform.scale(p.image.load("platformer/mr fucks.png"), (128, 128))
        self.position = p.Vector2(100, 100)
        self.rect = self.img.get_rect()
        self.max_speed = 600
        self.acceleration = 30
        self.friction = 60
        self.velocity = p.Vector2(0, 0)
        self.flipped = False

    def draw(self, screen):
        screen.blit(self.img, self.position)

    def move_processor(self, dt):
        keys = p.key.get_pressed()
        if keys[p.K_a]:
            if not self.flipped:
                self.img = p.transform.flip(self.img, True, False)
                self.flipped = True

            if self.velocity.x >= self.max_speed * -1:
                self.velocity.x += max(self.acceleration * -1, ((self.max_speed * -1) - self.velocity.x))
        else:
            if self.velocity.x < 0:
                self.velocity.x += max(self.friction, self.velocity.x)

        if keys[p.K_d]:
            if self.flipped:
                self.img = p.transform.flip(self.img, True, False)
                self.flipped = False

            if self.velocity.x <= self.max_speed:
                self.velocity.x += min(self.acceleration, self.max_speed - self.velocity.x)

        else:
            if self.velocity.x > 0:
                self.velocity.x -= min(self.friction, self.velocity.x)
        
        self.position += self.velocity * dt


        
            


        
        
    
