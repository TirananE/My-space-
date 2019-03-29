import arcade
from models import *

 
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        self.space = arcade.load_texture('space2.jpg')

        self.me = arcade.Sprite('me.png')
        self.me.set_position(500,300)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)
 
 
    def on_draw(self):
        arcade.start_render()

        arcade.draw_texture_rectangle(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,
                                    SCREEN_WIDTH,SCREEN_HEIGHT,self.space)
        self.me.draw()
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()