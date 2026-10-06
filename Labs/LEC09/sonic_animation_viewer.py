"""소닉 스프라이트 시트의 애니메이션을 순서대로 보여 준다."""

from pico2d import *

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
FRAME_INTERVAL = 0.1
ACTION_REPEAT_COUNT = 5
ACTION_PAUSE_SECONDS = 1.0
DEFAULT_SCALE = 4
IMAGE_PATH = 'sonic-sprite.png'


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image(IMAGE_PATH)
    close_canvas()


if __name__ == '__main__':
    main()
