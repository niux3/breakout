from pathlib import Path


class Config:
    BASE_ROOT: Path = Path(__file__).resolve().parent

    TITLE: str = 'Breakout'
    WIDTH: int = 1440
    HEIGHT: int = 1080
