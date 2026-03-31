from typing import Optional
import arcade
from src.config import Config
from src.sprites import (
    PaddleSprite,
    BallSprite
)
from src.views.base_view import BaseView


class GameView(BaseView):
    def __init__(self) -> None:
        super().__init__()
        self.background_sprites = arcade.SpriteList()
        self.foreground_sprites = arcade.SpriteList()

        self.paddle_sprite: Optional[PaddleSprite] = None
        self.shadow_sprite: Optional[PaddleSprite] = None

        self.ball_sprite: Optional[BallSprite] = None
        self.halo_ball_sprite: Optional[BallSprite] = None

        self.score_static_text: Optional[arcade.Text] = None
        self.live_static_text: Optional[arcade.Text] = None
        self.score_text: Optional[arcade.Text] = None
        self.lives_text: Optional[arcade.Text] = None

        self.score = 128_480
        self.lives = 3

        self.setup()

    def setup(self) -> None:
        self.load_font("fonts/RussoOne-Regular.ttf")
        self.score_static_text = arcade.Text(
            text="SCORE: ",
            x=20,
            y=Config.HEIGHT - 40,
            color=Config.COLOR_A,
            font_size=20,
            font_name="Russo One"
        )

        self.score_text = arcade.Text(
            text=str(self.score),
            x=130,
            y=Config.HEIGHT - 40,
            color=Config.COLOR_B,
            font_size=20,
            font_name="Russo One"
        )

        self.live_static_text = arcade.Text(
            text="LIVES: ",
            x=Config.WIDTH - 150,
            y=Config.HEIGHT - 40,
            color=Config.COLOR_A,
            font_size=20,
            font_name="Russo One"
        )

        self.lives_text = arcade.Text(
            text=str(self.lives),
            x=Config.WIDTH - 50,
            y=Config.HEIGHT - 40,
            color=Config.COLOR_B,
            font_size=20,
            font_name="Russo One"
        )

        paddle_texture = self.load_texture('images/paddle.png')
        shadow_paddle_texture = self.load_texture('images/shadow_paddle.png')
        ball_texture = self.load_texture('images/ball.png')
        halo_ball_texture = self.load_texture('images/shadow_ball.png')

        self.paddle_sprite = PaddleSprite(paddle_texture)
        self.paddle_sprite.set_position(Config.WIDTH / 2, 100)

        self.shadow_sprite = PaddleSprite(shadow_paddle_texture)
        self.shadow_sprite.set_position(Config.WIDTH / 2 + 15, 85)

        self.ball_sprite = BallSprite(ball_texture, scale=0.5, speed=10)
        self.ball_sprite.center_x = Config.WIDTH / 2
        self.ball_sprite.center_y = Config.HEIGHT / 2

        self.halo_ball_sprite = BallSprite(
            halo_ball_texture, scale=0.5, speed=10)
        self.halo_ball_sprite.center_x = Config.WIDTH / 2
        self.halo_ball_sprite.center_y = Config.HEIGHT / 2

        self.background_sprites.append(self.shadow_sprite)
        self.background_sprites.append(self.halo_ball_sprite)

        self.foreground_sprites.append(self.paddle_sprite)
        self.foreground_sprites.append(self.ball_sprite)

    def on_draw(self) -> None:
        self.clear()
        self.score_static_text.draw()
        self.score_text.draw()
        self.live_static_text.draw()
        self.lives_text.draw()

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
        self.shadow_sprite.center_x = self.paddle_sprite.center_x + 15
        self.shadow_sprite.center_y = self.paddle_sprite.center_y - 15

    def on_update(self, delta_time: float) -> None:
        self.background_sprites.update()
        self.foreground_sprites.update()
