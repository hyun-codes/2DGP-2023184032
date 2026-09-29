import math

from pico2d import *


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
FRAME_DELAY = 0.01
MOVE_SPEED = 4
CENTER_X = 400
CENTER_Y = 300
CIRCLE_RADIUS = 200
TRANSITION_POINT = (CENTER_X, CENTER_Y + CIRCLE_RADIUS)
LEFT = CENTER_X - CIRCLE_RADIUS
RIGHT = CENTER_X + CIRCLE_RADIUS
BOTTOM = CENTER_Y - CIRCLE_RADIUS
TOP = CENTER_Y + CIRCLE_RADIUS

character = None


def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(FRAME_DELAY)


def move_circle():
    circumference = 2 * math.pi * CIRCLE_RADIUS
    steps = round(circumference / MOVE_SPEED)

    for step in range(steps + 1):
        angle = math.pi / 2 + 2 * math.pi * step / steps
        x = CENTER_X + CIRCLE_RADIUS * math.cos(angle)
        y = CENTER_Y + CIRCLE_RADIUS * math.sin(angle)
        draw_character(x, y)


def move_line(start, end):
    start_x, start_y = start
    end_x, end_y = end
    distance = math.hypot(end_x - start_x, end_y - start_y)
    steps = max(1, round(distance / MOVE_SPEED))

    for step in range(steps + 1):
        ratio = step / steps
        x = start_x + (end_x - start_x) * ratio
        y = start_y + (end_y - start_y) * ratio
        draw_character(x, y)


def move_rectangle():
    top_left = (LEFT, TOP)
    bottom_left = (LEFT, BOTTOM)
    bottom_right = (RIGHT, BOTTOM)
    top_right = (RIGHT, TOP)

    move_line(TRANSITION_POINT, top_left)
    move_line(top_left, bottom_left)
    move_line(bottom_left, bottom_right)
    move_line(bottom_right, top_right)
    move_line(top_right, TRANSITION_POINT)


def main():
    global character

    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    character = load_image('character.png')

    draw_character(*TRANSITION_POINT)
    delay(1)

    move_circle()
    move_rectangle()
    delay(1)

    close_canvas()


if __name__ == '__main__':
    main()
