from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01
TRANSITION_POINT = (400, 500)

character = None


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def main():
    global character

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    character = load_image('character.png')

    draw_character(*TRANSITION_POINT)
    delay(1)

    close_canvas()


if __name__ == '__main__':
    main()
