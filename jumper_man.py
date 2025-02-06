import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCALING = 0.2

Title = "Jumper Man!!"

class JumperMan(arcade.Window):

    def __init__(self, width, height, title):

        super().__init__(width, height, title)

        self.player = None
        self.platform = None
    

    def setup(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)

        self.player = arcade.Sprite("SpriteImages/square.png", SCALING)
        self.player.center_x = self.width // 2
        self.player.center_y = self.height // 2

        self.add_platform()

    def add_platform(self):
        self.platform = arcade.Sprite("SpriteImages/rectangle.png", SCALING)

        self.platform.left = random.randint(0, self.width - 80)
        self.platform.bottom = random.randint(100, self.height - 100)
    
    def on_draw(self):
        arcade.start_render()
        self.platform.draw()
        self.player.draw()

    def on_key_press(self, symbol, modifiers):

        if symbol == arcade.key.LEFT:
            self.player.change_x = -5
        
        if symbol == arcade.key.RIGHT:
            self.player.change_x = 5
        
        if symbol == arcade.key.UP:
            self.player.change_y = 5
        
        if symbol == arcade.key.DOWN:
            self.player.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
            self.player.change_y = 0

        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.player.change_x = 0

    def on_update(self, delta_time: float):

        self.player.update()

        
        
        if self.player.collides_with_sprite(self.platform):
            
                if self.player.change_y < 0:

                    self.player.center_y = self.platform.top + (self.player.height // 2)
                    self.player.change_y = 0
                
        
        

game = JumperMan(SCREEN_WIDTH, SCREEN_HEIGHT, Title)

game.setup()

arcade.run()