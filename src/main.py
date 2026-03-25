import arcade
from src.omega_breakout_game import OmegaBreakoutGame
from src.views.game_view import GameView


if __name__ == '__main__':
    window = OmegaBreakoutGame()
    game = GameView()
    window.show_view(game)
    arcade.run()
