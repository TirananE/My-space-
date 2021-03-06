import arcade
from models2 import World , Me
 
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 700
PAGE_1 = 0
GAME_RUN = 2

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

        self.welcome = arcade.Sprite('welcome2.png')
        self.welcome.set_position(350,350)
        self.current_page = PAGE_1

        self.background = arcade.Sprite('space5-crop.png')
        #frame = 28 pixel
        self.background.set_position(350,350)

        self.world = World(width,height)
        self.me_sprite = ModelSprite('enemy41.png',model=self.world.me)
        self.food_sprite = ModelSprite('food1.png',model=self.world.food )
        self.enemy_sprite = ModelSprite('enemy_angryface11.png',model=self.world.enemy)
        self.enemy2_sprite = ModelSprite('enemy_yellow2.png',model=self.world.enemy2)



        self.game_over = ModelSprite('game over1.png')
        self.game_over.set_position(350,350)


    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.ENTER:
            self.current_page = GAME_RUN
        else:
            if not self.world.is_started():
                self.world.start()
            self.world.on_key_press(key, key_modifiers)

    def draw_page_1(self):
        texture = arcade.load_texture('welcome2.png')
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT //2, SCREEN_WIDTH, SCREEN_HEIGHT, texture)

    def draw_game(self):
        #arcade.start_render()

        # self.welcome.draw()
        
        self.background.draw()
        self.food_sprite.draw()

        self.me_sprite.draw()

        arcade.draw_text(str(self.world.show_score) , self.width - 180, self.height - 80,
                            arcade.color.BLACK, 20)

        if self.world.score >= 70 :
            self.enemy_sprite.draw()

        if self.world.score >= 130 :
            self.enemy2_sprite.draw()


        if self.world.state == 3:
            self.game_over.draw()
            arcade.draw_text(str(f'YOUR {self.world.show_score}') , self.width - 485, self.height - 370,
                            arcade.color.WHITE, 30)

    def on_draw(self):
        # arcade.start_render()

        # # self.welcome.draw()
        
        # self.background.draw()
        # self.food_sprite.draw()

        # self.me_sprite.draw()

        # arcade.draw_text(str(self.world.show_score) , self.width - 180, self.height - 80,
        #                     arcade.color.BLACK, 20)

        # if self.world.score >= 80 :
        #     self.enemy_sprite.draw()

        # if self.world.score >= 130 :
        #     self.enemy2_sprite.draw()


        # if self.world.state == 3:
        #     self.game_over.draw()
        #     arcade.draw_text(str(f'YOUR {self.world.show_score}') , self.width - 485, self.height - 370,
        #                     arcade.color.WHITE, 30)

        arcade.start_render()

        if self.current_page == PAGE_1:
            self.draw_page_1()
        elif self.current_page == GAME_RUN:
            self.draw_game()
        
    def update(self, delta):
        self.world.update(delta)
 
 
if __name__ == '__main__':
    window = SpaceGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()