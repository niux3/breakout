import arcade
from src.config import Config


class PaddleSprite(arcade.Sprite):
    def __init__(self, texture: arcade.Texture, scale: float = 1.0) -> None:
        super().__init__(texture, scale)
        self.center_x = Config.WIDTH / 2
        self.center_y = 20
