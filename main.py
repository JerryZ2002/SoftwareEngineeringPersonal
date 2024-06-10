# main.py
from funny_json_explorer import FunnyJsonExplorer
from factory import IconFactory, TreeStyleFactory, RectangleStyleFactory


def main():
    icon_factory = (IconFactory("poker-face"), IconFactory("chess"), IconFactory("star"))
    style_factory = (TreeStyleFactory(), RectangleStyleFactory())
    json_file = "example.json"
    for icon in icon_factory:
        for style in style_factory:
            print(f"Icon: {icon.icon_family}, Style: {style.__class__.__name__.replace('StyleFactory', '')}")
            explorer = FunnyJsonExplorer(style, icon)
            explorer.show(json_file, style)
            print()


if __name__ == "__main__":
    main()
