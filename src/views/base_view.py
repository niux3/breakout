import arcade
from src.config import Config


class BaseView(arcade.View):
    _resources_initialized = False

    def __init__(self) -> None:
        super().__init__()

        if not BaseView._resources_initialized:
            Config.setup_resource()
            BaseView._resources_initialized = True

    def load_texture(self, path: str) -> arcade.Texture:
        return arcade.load_texture(Config.get_asset(path))

    def load_soud(self, path: str) -> arcade.Sound:
        return arcade.load_sound(Config.get_asset(path))
