from typing import Optional
import arcade
from src.config import Config
from src.sprites.paddle_sprite import PaddleSprite
from src.views.base_view import BaseView


class GameView(BaseView):
    def __init__(self) -> None:
        super().__init__()
        self.background_sprites = arcade.SpriteList()
        self.foreground_sprites = arcade.SpriteList()

        self.paddle_sprite: Optional[PaddleSprite] = None
        self.shadow_sprite: Optional[PaddleSprite] = None

        self.setup()

    def setup(self) -> None:
        paddle_texture = self.load_texture('images/paddle.png')
        shadow_paddle_texture = self.load_texture('images/shadow_paddle.png')

        self.paddle_sprite = PaddleSprite(paddle_texture)
        self.paddle_sprite.set_position(Config.WIDTH / 2, 100)

        self.shadow_sprite = PaddleSprite(shadow_paddle_texture)
        self.shadow_sprite.set_position(Config.WIDTH / 2 + 15, 85)

        self.background_sprites.append(self.shadow_sprite)
        self.foreground_sprites.append(self.paddle_sprite)

    def on_draw(self) -> None:
        self.clear()
        self.background_sprites.draw()
        self.foreground_sprites.draw()

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.ESCAPE:
            arcade.exit()

    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int) -> None:
        left_limit = self.paddle_sprite.width / 2
        right_limit = Config.WIDTH - self.paddle_sprite.width / 2
        new_x = max(left_limit, min(x, right_limit))

        self.paddle_sprite.center_x = new_x
        self.shadow_sprite.center_x = x + 15
        self.shadow_sprite.center_y = self.paddle_sprite.center_y - 15

    def on_update(self, delta_time: float) -> None:
        self.background_sprites.update()
        self.foreground_sprites.update()
