import arcade
from src.config import Config
from src.views.gameview import GameView


if __name__ == '__main__':
    window = arcade.Window(Config.WIDTH, Config.HEIGHT, Config.TITLE)
    game = GameView()
    window.show_view(game)
    arcade.run()
