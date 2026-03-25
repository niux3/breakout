from pathlib import Path
import arcade


class Config:
    BASE_ROOT: Path = Path(__file__).resolve().parent

    TITLE: str = 'Omega Breakout'
    WIDTH: int = 1440
    HEIGHT: int = 1080

    BG_COLOR = (8, 24, 49, 255)

    @classmethod
    def setup_resource(cls) -> None:
        assets_path = cls.BASE_ROOT / 'assets'
        arcade.resources.add_resource_handle('assets', str(assets_path))

    @classmethod
    def get_asset(cls, path: str) -> str:
        return f":assets:{path}"
