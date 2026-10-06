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
FIRST_FRAME = (1, 447, 29, 39)


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

    running = True
    for _ in range(100):
        clear_canvas()
        draw_frame(sprite_sheet, FIRST_FRAME)
        update_canvas()

        running = handle_events()
        if not running:
            break
        delay(0.01)

    close_canvas()


if __name__ == '__main__':
    main()
