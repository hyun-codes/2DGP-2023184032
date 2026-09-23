# 실습 과제 진행
from pico2d import *

open_canvas(800,600)
boy = load_image('character.png')

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)

def move_circle():
    for degree in range(361):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_boy(x,y)
    pass

def move_top():
     for x in range(200, 601, 5):
        draw_boy(x, 500)

def move_right():
    for y in range(500, 99, -5):
        draw_boy(600, y)  

def move_bottom():
    for x in range(600, 199, -5):
        draw_boy(x, 100)

def move_left():
    for y in range(100, 501, 5):
        draw_boy(200, y)

def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    
    pass

def move_triangle_left():
    for x in range(400, 199, -5):
        y = 2 * x - 300
        draw_boy(x, y)

def move_triangle_bottom():
    for x in range(200, 601, 5):
        draw_boy(x, 100)

def move_triangle_right():
    for x in range(600, 399, -5):
        y = -2 * x + 1300
        draw_boy(x, y)

def move_triangle():
    move_triangle_left()
    move_triangle_bottom()
    move_triangle_right()


def draw_boy(x, y):
    clear_canvas()
    boy.draw(x,y)
    update_canvas()
    delay(0.01)

while True:
    #move_circle()
    #move_rectangle()
    move_triangle()

    pass

close_canvas()
