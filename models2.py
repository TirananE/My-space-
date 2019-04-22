import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
 
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) }

class Me:

    DIR_HORIZONTAL = 0
    DIR_VERTICAL = 1

    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.direction = Me.DIR_VERTICAL
        self.angle = 0

    def swith_direction(self):
        if self.direction == Me.DIR_HORIZONTAL:
            self.direction = Me.DIR_VERTICAL
            self.angle = 0
        else:
            self.direction = Me.DIR_HORIZONTAL
            self.angle = -90

    def update(self, delta):
        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]

class World:

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.me = Me(self,350,350)

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

        