import pygame as p

class Player:
    def __init__(self, level):
        self.img = p.transform.scale(p.image.load("platformer/mr fucks.png"), (128, 128))
        self.rect = self.img.get_rect().inflate(-43, 0)
        self.position = p.Vector2(150, 150)
        self.rect.x = self.position.x
        self.rect.y = self.position.y

        self.collision_rect = p.Rect((self.rect.x + self.rect.width // 2), (self.rect.y), (self.rect.width // 2), self.rect.height)
        self.max_speed = 16
        self.acceleration = 4
        self.friction = 2
        self.gravity = 3
        self.max_fall_speed = 25
        self.jump_power = 40
        self.velocity = p.Vector2(0, 0)
        self.on_floor = False

        self.flipped = False

        self.level = level


    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))

    
    def event_processor(self, event):
            if event.type == p.KEYDOWN:
                if event.key == p.K_SPACE and self.on_floor:
                    self.velocity.y = self.jump_power * -1


    def move_processor(self):
        keys = p.key.get_pressed()
        if keys[p.K_a]:
            if not self.flipped:
                self.img = p.transform.flip(self.img, True, False)
                self.flipped = True
            if self.velocity.x > self.max_speed * -1:
                self.velocity.x -= self.acceleration

        if keys[p.K_d]:
            if self.flipped:
                self.img = p.transform.flip(self.img, True, False)
                self.flipped = False
            if self.velocity.x < self.max_speed:
                self.velocity.x += self.acceleration
        
        if self.velocity.y < self.max_fall_speed:
            self.velocity.y += self.gravity
        
        if self.velocity.x > 0:
            self.velocity.x -= self.friction
        elif self.velocity.x < 0:
            self.velocity.x += self.friction


        collisions = self.collision_process()
        if collisions:
            if collisions['bottom'] == True:
                self.on_floor = True
                self.velocity.y = 0
            else:
                self.on_floor = False
            
            if collisions['top'] == True:
                self.velocity.y = 0


    def check_collision(self):
        collided_list = []
        for row in self.level.datamap:
            for tile in row:
                if tile != None:
                    if self.collision_rect.colliderect(tile.rect):
                        collided_list.append(tile.rect)
        return collided_list
    
    
    def collision_process(self):
        collision_types = {'top': False, 'bottom': False, 'left': False, 'right': False}

        self.collision_rect.x += self.velocity.x
        collisions = self.check_collision()
        for tile in collisions:
            if self.velocity.x > 0:
                self.collision_rect.right = tile.left
                collision_types['right'] = True
            elif self.velocity.x < 0:
                self.collision_rect.left = tile.right
                collision_types['left'] = True
            
        self.collision_rect.y += self.velocity.y
        collisions = self.check_collision()
        for tile in collisions:
            if self.velocity.y > 0:
                self.collision_rect.bottom = tile.top
                collision_types['bottom'] = True
            elif self.velocity.y < 0:
                self.collision_rect.top = tile.bottom
                collision_types['top'] = True

        self.rect.x = self.collision_rect.x - (self.rect.width // 2)
        self.rect.y = self.collision_rect.y
        return collision_types
    






    

                        
                        


        
            


        
        
    
