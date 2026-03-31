from typing import Callable, Optional, Union
import arcade
from src.config import Config


class BaseView(arcade.View):
    _resources_initialized = False

    def __init__(self) -> None:
        super().__init__()
        if not BaseView._resources_initialized:
            Config.setup_resource()
            BaseView._resources_initialized = True

    def _load_resource(self, resource_type: str, path: str, loader_func: Callable) -> Optional[Union[arcade.Texture, arcade.Sound, bool]]:
        """
        Charge une ressource de manière générique.

        Args:
            resource_type: Type de ressource ("Texture", "Sound", "Font")
            path: Chemin vers la ressource
            loader_func: Fonction de chargement Arcade correspondante

        Returns:
            - Pour Texture/Sound: l'objet chargé ou None
            - Pour Font: True si succès, False/None si erreur
        """
        try:
            fullpath = Config.get_asset(path)
            if resource_type == 'Font':
                loader_func(fullpath)
                return True
            return loader_func(fullpath)
        except FileNotFoundError:
            print(f"{resource_type} not found: {path}")
            return None
        except Exception as e:
            print(f"Error loading {resource_type} {path}: {e}")
            return None

    def load_texture(self, path: str) -> Optional[arcade.Texture]:
        """Charge une texture depuis le dossier assets"""
        return self._load_resource("Texture", path, arcade.load_texture)

    def load_sound(self, path: str) -> Optional[arcade.Sound]:
        """Charge un son depuis le dossier assets"""
        return self._load_resource("Sound", path, arcade.load_sound)

    def load_font(self, path: str) -> Optional[bool]:
        """Charge une police depuis le dossier assets"""
        return self._load_resource("Font", path, arcade.load_font)
