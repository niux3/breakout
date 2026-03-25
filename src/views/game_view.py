from src.views.base_view import BaseView


class GameView(BaseView):
    def __init__(self) -> None:
        super().__init__()
        paddle_texture = self.load_texture('images/paddle.png')

    def on_draw(self) -> None:
        self.clear()
