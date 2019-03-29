import arcade.key
from random import randint

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }
class Me:
    MOVE_WAIT = 0.2
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y
        self.wait_time = 0
        self.direction = DIR_RIGHT
 
    def update(self, delta):
        self.wait_time += delta
 
        if self.wait_time < Me.MOVE_WAIT:
            return
 
        if self.x > self.world.width:
            self.x = 0
            
        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]
        
        self.wait_time = 0

 
''' 
class Heart:
    def __init__(self, world):
        self.world = world
        self.x = 0
        self.y = 0
 
    def random_position(self):
        centerx = self.world.width // 2
        centery = self.world.height // 2
 
        self.x = centerx + randint(-15,15)
        self.y = centerx + randint(-15,15)
'''
class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
 
        self.me = Me(self, 100, 100)

        #self.heart = Heart(self)
        #self.heart.random_position()

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT:
            self.me.direction = DIR_RIGHT
        elif key == arcade.key.DOWN:
            self.me.direction = DIR_DOWN
        elif key == arcade.key.LEFT:
            self.me.direction = DIR_LEFT
        elif key == arcade.key.UP:
            self.me.direction = DIR_UP
 
    def update(self, delta):
        self.me.update(delta)
