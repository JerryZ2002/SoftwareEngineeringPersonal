# funny_json_explorer.py
from utils import load_json
from json_component import Leaf

MAX_LENGTH = 40


class FunnyJsonExplorer:
    def __init__(self, style_factory, icon_factory):
        self.style_factory = style_factory
        self.icon_factory = icon_factory

    def _load(self, json_file):
        return load_json(json_file)

    def show(self, json_file, style):
        data = self._load(json_file)
        container = self.style_factory.create_container(self.icon_factory, "root", 0)
        self._parse_json(data, container, style)
        container.draw(prefix='', max_length=MAX_LENGTH)

    def _parse_json(self, data, container, style, level=1):
        for key, value in data.items():
            if isinstance(value, dict):
                sub_container = self.style_factory.create_container(self.icon_factory, key, level)
                container.add(sub_container)
                self._parse_json(value, sub_container, style, level + 1)
            else:
                if value is not None:
                    key = f"{key}: {value}"
                leaf = Leaf(key, self.icon_factory.get_icon(is_leaf=True))
                container.add(leaf)
