import arcade.key
from random import randint

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4

VELOCITY = 4
DIR_OFFSET = { DIR_UP: (0,VELOCITY),
               DIR_RIGHT: (VELOCITY,0),
               DIR_DOWN: (0,-VELOCITY),
               DIR_LEFT: (-VELOCITY,0) }

# class Model:
#     def __init__(self, world, x, y, angle):
#         self.world = world
#         self.x = x
#         self.y = y

#     def hit(self, other, hit_size):
#         return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)

class Me:

    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1
    BLOCK_SIZE = 10

    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Me.DIR_VERTICAL
        self.has_eaten = False

    def can_eat(self, food):
        if food.x - 10 <= self.x <= food.x + 10 and food.y - 10 <= self.y <= food.y + 10:
            return True
        return False

    def swith_direction(self):
        if self.direction == Me.DIR_HORIZONTAL:
            self.direction = Me.DIR_VERTICAL
        else:
            self.direction = Me.DIR_HORIZONTAL

    def update(self, delta):
        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]

class Food:
    def __init__(self, world, x, y):
        self.world = world
        self.x = x
        self.y = y

    def random_location(self):
        centerx = self.world.width // 2
        centery = self.world.height // 2
 
        self.x = centerx + randint(-15,15) * Me.BLOCK_SIZE
        self.y = centery + randint(-15,15) * Me.BLOCK_SIZE

class World:

    STATE_FROZEN = 1
    STATE_STARTED = 2
    STATE_DEAD = 3

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.me = Me(self,350,350)
        self.food = Food(self, 600, 600)
        self.food.random_location()
        self.state = World.STATE_FROZEN

    def start(self):
        self.state = World.STATE_STARTED
 
    def freeze(self):
        self.state = World.STATE_FROZEN     
 
    def is_started(self):
        return self.state == World.STATE_STARTED

    def die(self):
        self.state = World.STATE_DEAD
 
    def is_dead(self):
        return self.state == World.STATE_DEAD

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
        if self.state in [World.STATE_FROZEN, World.STATE_DEAD]:
            return
        if self.me.can_eat(self.food):
            self.food.random_location()
            self.me.has_eaten = True
        self.me.update(delta)
        

        