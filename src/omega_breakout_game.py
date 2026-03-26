import arcade
from src.config import Config


class OmegaBreakoutGame(arcade.Window):
    def __init__(self) -> None:
        super().__init__(
            Config.WIDTH,
            Config.HEIGHT,
            Config.TITLE
        )
        self.background_color = Config.BG_COLOR
        self.set_mouse_visible(False)
