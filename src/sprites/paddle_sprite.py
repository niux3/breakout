import arcade


class PaddleSprite(arcade.Sprite):
    def __init__(self, texture: arcade.Texture, scale: float = 1.0) -> None:
        super().__init__(texture, scale)

    def set_position(self, x: int, y: int) -> None:
        self.center_x = x
        self.center_y = y
