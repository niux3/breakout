import arcade
import random


class BallSprite(arcade.Sprite):
    def __init__(self, texture: arcade.Texture, scale: float = 1.0, speed: float = 5.0) -> None:
        super().__init__(texture, scale)
        self.speed_x: float = speed
        self.speed_y: float = speed

    def update(self, delta_time: float = 1 / 60, *args, **kwargs) -> None:
        self.center_x += self.speed_x
        self.center_y += self.speed_y

    def bounce_x(self) -> None:
        self.speed_x *= -1

    def bounce_y(self) -> None:
        self.speed_y *= -1

    def reset_position(self, x: float, y: float) -> None:
        self.center_x = x
        self.center_y = y
        self.speed_x = abs(self.speed_x)
        self.speed_y = abs(self.speed_y)
