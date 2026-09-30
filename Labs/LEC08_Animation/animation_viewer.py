from pathlib import Path

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
DRAW_SCALE = 4.0

# 가산점: 각 프레임의 (left, top, width, height)를 개별 정의한다.
IDLE_FRAMES = (
    (91, 1202, 76, 97), (171, 1203, 76, 96), (251, 1204, 76, 95),
    (331, 1203, 76, 96), (412, 1203, 76, 96), (492, 1202, 76, 97),
    (572, 1202, 75, 97), (651, 1202, 76, 97), (731, 1202, 76, 97),
    (811, 1202, 76, 97), (891, 1202, 76, 97),
)


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


def draw_frame(sprite_sheet, frame):
    rectangle = to_clip_rectangle(frame, sprite_sheet.h)
    width, height = frame[2:]
    clear_canvas()
    sprite_sheet.clip_draw(
        *rectangle, CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
        round(width * DRAW_SCALE), round(height * DRAW_SCALE),
    )
    update_canvas()


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_path = Path(__file__).with_name('BlueKnightSpriteSheet.png')
    sprite_sheet = load_image(str(sprite_path))
    while handle_events():
        draw_frame(sprite_sheet, IDLE_FRAMES[0])
        delay(0.01)
    close_canvas()


if __name__ == '__main__':
    main()
