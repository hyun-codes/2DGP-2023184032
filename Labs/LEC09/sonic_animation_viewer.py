"""소닉 스프라이트 시트의 애니메이션을 순서대로 보여 준다."""

from pico2d import *

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
FRAME_INTERVAL = 0.1
ACTION_REPEAT_COUNT = 5
ACTION_PAUSE_SECONDS = 1.0
DEFAULT_SCALE = 4
CANVAS_MARGIN = 40
IMAGE_PATH = 'sonic-sprite.png'

# 프레임 좌표 형식: (왼쪽 x, 아래쪽 y, 너비, 높이)
ACTIONS = (
    {
        'name': '걷기와 달리기 전환',
        'frames': (
            (1, 447, 29, 39),
            (31, 447, 26, 38),
            (58, 447, 28, 39),
            (86, 447, 30, 38),
            (118, 447, 30, 38),
            (150, 447, 30, 38),
            (182, 447, 29, 38),
            (211, 448, 29, 38),
            (240, 448, 29, 38),
            (270, 448, 24, 32),
            (302, 448, 29, 26),
        ),
    },
)


def draw_frame(sprite_sheet, frame):
    x, y, width, height = frame
    scale = min(DEFAULT_SCALE,
                (CANVAS_WIDTH - CANVAS_MARGIN * 2) / width,
                (CANVAS_HEIGHT - CANVAS_MARGIN * 2) / height)
    sprite_sheet.clip_draw(x, y, width, height,
                           CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2,
                           width * scale, height * scale)


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def main():
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    sprite_sheet = load_image(IMAGE_PATH)

    frames = ACTIONS[0]['frames']
    frame_index = 0
    last_frame_time = get_time()
    running = True
    while running:
        current_time = get_time()
        if current_time - last_frame_time >= FRAME_INTERVAL:
            frame_index = (frame_index + 1) % len(frames)
            last_frame_time = current_time

        clear_canvas()
        draw_frame(sprite_sheet, frames[frame_index])
        update_canvas()

        running = handle_events()
        delay(0.001)

    close_canvas()


if __name__ == '__main__':
    main()
