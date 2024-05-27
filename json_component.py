# json_component.py
from abc import ABC, abstractmethod


class JsonComponent(ABC):
    @abstractmethod
    def draw(self, prefix='', max_length=0):
        pass

class Leaf(JsonComponent):
    def __init__(self, name, icon=None):
        self.name = name
        self.icon = icon

    def draw(self, prefix='', max_length=0):
        line = f"{prefix}  {self.icon} {self.name} "
        line += '─' * (max_length - len(line) - 1) + "┤"
        print(line)
