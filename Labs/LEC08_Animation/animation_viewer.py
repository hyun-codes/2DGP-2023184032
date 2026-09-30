from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600


def to_clip_rectangle(frame, sheet_height):
    """이미지 위쪽 기준 좌표를 pico2d의 아래쪽 기준 좌표로 변환한다."""
    left, top, width, height = frame
    return left, sheet_height - top - height, width, height


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_path = Path(__file__).with_name('BlueKnightSpriteSheet.png')
    sprite_sheet = load_image(str(sprite_path))
    while handle_events():
        clear_canvas()
        update_canvas()
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()
