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
PLAYING = 'playing'
PAUSED_BETWEEN_ACTIONS = 'paused_between_actions'

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
    {
        'name': '빠르게 달리기',
        'frames': (
            (8, 408, 26, 37),
            (37, 408, 27, 37),
            (65, 407, 31, 38),
            (97, 408, 37, 37),
            (135, 410, 32, 35),
            (170, 408, 32, 38),
            (206, 408, 26, 38),
            (238, 408, 24, 37),
            (263, 408, 30, 37),
            (295, 408, 36, 37),
            (334, 409, 32, 36),
            (370, 408, 29, 38),
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

    action_index = 0
    frames = ACTIONS[action_index]['frames']
    frame_index = 0
    completed_repeats = 0
    playback_state = PLAYING
    last_frame_time = get_time()
    pause_started_at = None
    running = True
    while running:
        current_time = get_time()
        if (playback_state == PLAYING and
                current_time - last_frame_time >= FRAME_INTERVAL):
            next_frame_index = (frame_index + 1) % len(frames)
            if next_frame_index == 0:
                completed_repeats += 1
                if completed_repeats >= ACTION_REPEAT_COUNT:
                    playback_state = PAUSED_BETWEEN_ACTIONS
                    frame_index = len(frames) - 1
                    pause_started_at = current_time
                else:
                    frame_index = next_frame_index
            else:
                frame_index = next_frame_index
            last_frame_time = current_time
        elif (playback_state == PAUSED_BETWEEN_ACTIONS and
              current_time - pause_started_at >= ACTION_PAUSE_SECONDS):
            action_index = (action_index + 1) % len(ACTIONS)
            frames = ACTIONS[action_index]['frames']
            playback_state = PLAYING
            frame_index = 0
            completed_repeats = 0
            last_frame_time = current_time
            pause_started_at = None

        clear_canvas()
        draw_frame(sprite_sheet, frames[frame_index])
        update_canvas()

        running = handle_events()
        delay(0.001)

    close_canvas()


if __name__ == '__main__':
    main()
