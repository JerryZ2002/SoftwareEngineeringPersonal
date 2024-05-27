# factory.py
from style import TreeStyle, RectangleStyle
from abc import abstractmethod


class IconFactory:
    def __init__(self, icon_family):
        self.icon_family = icon_family

    def get_icon(self, is_leaf=False):
        if self.icon_family == "poker-face":
            return '♠' if is_leaf else '♦'
        elif self.icon_family == "chess":
            return '♟' if is_leaf else '♜'
        elif self.icon_family == "star":
            return '☆' if is_leaf else '✬'
        else:
            raise ValueError(f"Unknown icon family: {self.icon_family}")


class AbstractStyleFactory:
    @abstractmethod
    def create_container(self, icon_factory, name, level):
        pass


class TreeStyleFactory(AbstractStyleFactory):
    def create_container(self, icon_factory, name, level):
        return TreeStyle(icon_factory, name, level)


class RectangleStyleFactory(AbstractStyleFactory):
    def create_container(self, icon_factory, name, level):
        return RectangleStyle(icon_factory, name, level)
