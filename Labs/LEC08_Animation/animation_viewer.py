from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_path = Path(__file__).with_name('BlueKnightSpriteSheet.png')
    sprite_sheet = load_image(str(sprite_path))
    close_canvas()


if __name__ == '__main__':
    main()
