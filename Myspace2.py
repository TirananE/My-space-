import arcade
from models2 import World , Me
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)
 
        super().__init__(*args, **kwargs)
 
    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)
 
    def draw(self):
        self.sync_with_model()
        super().draw()
 
class SpaceGameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
 
        arcade.set_background_color(arcade.color.BLACK)

        self.background = arcade.Sprite('space5-crop.png')
        #frame = 28 pixel
        self.background.set_position(350,350)

        self.world = World(width,height)
        self.me_sprite = ModelSprite('enemy41.png',model=self.world.me)
        self.food_sprite = ModelSprite('food1.png',model=self.world.food )

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_draw(self):
        arcade.start_render()
        self.background.draw()
        self.me_sprite.draw()
        self.food_sprite.draw()

    def update(self, delta):
        self.world.update(delta)
        # self.me_sprite.set_position(self.world.me.x, self.world.me.y)
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()