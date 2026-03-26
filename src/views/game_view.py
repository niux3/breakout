from typing import Optional
import arcade
from src.sprites.paddle_sprite import PaddleSprite
from src.views.base_view import BaseView


class GameView(BaseView):
    def __init__(self) -> None:
        super().__init__()
        self.all_sprites_list = arcade.SpriteList()

        self.paddle_sprite: Optional[PaddleSprite] = None

        self.setup()

    def setup(self) -> None:
        paddle_texture = self.load_texture('images/paddle.png')
        self.paddle_sprite = PaddleSprite(paddle_texture)

        self.all_sprites_list.append(self.paddle_sprite)

    def on_draw(self) -> None:
        self.clear()
        self.all_sprites_list.draw()
