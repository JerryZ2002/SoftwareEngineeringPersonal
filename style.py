# style.py
from abc import abstractmethod


class Style:
    def __init__(self, icon_factory, name, level):
        self.name = name
        self.level = level
        self.icon_factory = icon_factory
        self.children = []

    def add(self, component):
        self.children.append(component)

    @abstractmethod
    def draw(self, prefix='', max_length=0):
        pass


class TreeStyle(Style):
    def draw(self, prefix='', max_length=0):
        line = f"{prefix}├─ {self.icon_factory.get_icon()} {self.name} "
        if self.level == 0:
            line = f"└─ {self.icon_factory.get_icon()} {self.name} "
        if self.level == 0 or len(self.children) == 0:
            line += ' ' * (max_length - len(line) - 1)
        else:
            line += ' ' * (max_length - len(line) - 1)
        print(line)
        new_prefix = prefix + "   "
        for i, child in enumerate(self.children):
            child.draw(new_prefix, 0)


class RectangleStyle(Style):
    def draw(self, prefix='', max_length=0):
        line = f"{prefix}├─ {self.icon_factory.get_icon()} {self.name} "
        if self.level == 0:
            line = f"┌─ {self.icon_factory.get_icon()} {self.name} "
        if self.level == 0 or len(self.children) == 0:
            line += '─' * (max_length - len(line) - 1) + "┐"
        else:
            line += '─' * (max_length - len(line) - 1) + "┤"
        print(line)
        new_prefix = prefix + "│  "
        for i, child in enumerate(self.children):
            child.draw(new_prefix, max_length)
        if self.level == 0 and len(self.children) > 0:
            print("└" + "─" * (max_length - 2) + "┘")
