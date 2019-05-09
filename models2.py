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

class Model:
    def __init__(self, world, x, y, angle):
        self.world = world
        self.x = x
        self.y = y

    def hit(self, other, hit_size):
        return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)


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
        if food.x - 30 <= self.x <= food.x + 30 and food.y - 30 <= self.y <= food.y + 30:
            return True
        return False

    def hit_enemy(self,enemy):
        if enemy.x - 60 <= self.x <= enemy.x + 60 and enemy.y - 60 <= self.y <= enemy.y + 60:
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


class Enemy:
 
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 2
        self.vy = 4
 
 
    def update(self, delta):

        self.x += self.vx
        self.y += self.vy

        if self.x > self.world.width - 60 or self.x < 60:
            self.vx = -self.vx
        if self.y > self.world.width - 58 or self.y < 58:
            self.vy = -self.vy

class Enemy2:
 
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.vx = 7
        self.vy = 10
 
 
    def update(self, delta):

        self.x += self.vx
        self.y += self.vy

        if self.x > self.world.width - 60 or self.x < 60:
            self.vx = -self.vx
        if self.y > self.world.width - 60 or self.y < 60:
            self.vy = -self.vy



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
        self.enemy = Enemy(self,200,200)
        self.enemy2 = Enemy2(self,200,200)

        self.score = 0
        self.show_score = f'SCORE: {self.score}'

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
        if self.me.x+40 >= self.width - 30 :
            self.die()
        if self.me.x-40 <= 30 :
            self.die()
        if self.me.y+36.5 >= self.height - 30 :
            self.die()
        if self.me.y-36.5 <= 30 :
            self.die()
        

        if self.me.can_eat(self.food):
            self.food.random_location()
            self.me.has_eaten = True
            self.score += 10
            self.show_score = f'SCORE: {self.score}'

        self.enemy.update(delta)
        self.enemy2.update(delta)
        self.me.update(delta)