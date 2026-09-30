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

WALK_FRAMES = (
    (105, 908, 76, 98),
    (201, 909, 78, 96),
    (293, 909, 84, 95),
    (389, 909, 86, 96),
    (485, 910, 88, 96),
    (591, 909, 79, 97),
    (689, 908, 79, 98),
    (788, 908, 77, 97),
    (887, 908, 76, 97),
    (982, 908, 77, 97),
)

RUN_FRAMES = (
    (89, 813, 97, 90),
    (193, 812, 92, 95),
    (301, 812, 83, 91),
    (401, 812, 82, 94),
    (500, 812, 82, 95),
    (599, 812, 82, 93),
    (698, 813, 81, 92),
    (796, 813, 82, 94),
    (895, 813, 82, 95),
    (984, 813, 92, 94),
)

JUMP_FRAMES = (
    (102, 1102, 76, 97),
    (197, 1101, 78, 96),
    (292, 1100, 79, 95),
    (386, 1100, 80, 96),
    (474, 1100, 88, 96),
    (569, 1100, 89, 96),
    (668, 1100, 85, 97),
    (767, 1101, 81, 97),
    (865, 1101, 78, 97),
    (962, 1102, 77, 97),
)

# 가산점: 동작별 프레임 수는 해당 튜플의 길이로 결정된다.
ANIMATIONS = (
    ('Jump', JUMP_FRAMES, 0.1),
    ('Run', RUN_FRAMES, 0.08),
    ('Walk', WALK_FRAMES, 0.11),
    ('Idle', IDLE_FRAMES, 0.14),
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
    running = True
    while running:
        for _, frames, frame_seconds in ANIMATIONS:
            for frame in frames:
                running = handle_events()
                if not running:
                    break
                draw_frame(sprite_sheet, frame)
                delay(frame_seconds)
            if not running:
                break
    close_canvas()


if __name__ == '__main__':
    main()
