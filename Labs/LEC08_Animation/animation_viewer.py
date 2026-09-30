from pathlib import Path
from time import monotonic

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
DRAW_SCALE = 4.0
REPEAT_COUNT = 5
PAUSE_SECONDS = 1.0

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

ATTACK_FRAMES = (
    (132, 339, 76, 97),
    (252, 339, 85, 97),
    (367, 335, 107, 100),
    (496, 316, 98, 119),
    (617, 339, 105, 96),
    (730, 339, 121, 96),
    (871, 339, 108, 96),
    (1025, 339, 82, 96),
    (1156, 339, 80, 97),
    (1286, 339, 78, 97),
)

SUMMON_FRAMES = (
    (90, 689, 96, 120),
    (194, 688, 97, 121),
    (298, 688, 99, 121),
    (403, 689, 98, 120),
    (508, 689, 97, 120),
    (612, 688, 99, 121),
    (717, 689, 99, 120),
    (822, 689, 98, 120),
    (927, 689, 97, 120),
)

# 가산점: 동작별 프레임 수는 해당 튜플의 길이로 결정된다.
ANIMATIONS = (
    ('Idle', IDLE_FRAMES, 0.14),
    ('Walk', WALK_FRAMES, 0.11),
    ('Run', RUN_FRAMES, 0.08),
    ('Jump', JUMP_FRAMES, 0.10),
    ('Attack', ATTACK_FRAMES, 0.10),
    ('Summon', SUMMON_FRAMES, 0.12),
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


def play_animation(sprite_sheet, animation):
    name, frames, frame_seconds = animation
    print(f'{name}: {len(frames)} frames, {REPEAT_COUNT} repeats')
    for _ in range(REPEAT_COUNT):
        for frame in frames:
            if not show_frame_for(sprite_sheet, frame, frame_seconds):
                return False
    return show_frame_for(sprite_sheet, frames[-1], PAUSE_SECONDS)


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        hide_lattice()
        sprite_path = Path(__file__).with_name('BlueKnightSpriteSheet.png')
        sprite_sheet = load_image(str(sprite_path))
        while True:
            for animation in ANIMATIONS:
                if not play_animation(sprite_sheet, animation):
                    return
    finally:
        close_canvas()


def show_frame_for(sprite_sheet, frame, seconds):
    """정지 중에도 창 닫기/ESC 이벤트를 계속 처리한다."""
    deadline = monotonic() + seconds
    while monotonic() < deadline:
        if not handle_events():
            return False
        draw_frame(sprite_sheet, frame)
        delay(0.005)
    return True


if __name__ == '__main__':
    main()
