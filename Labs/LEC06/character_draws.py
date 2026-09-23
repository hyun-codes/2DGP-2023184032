# 실습 과제 진행
from pico2d import *

open_canvas(800,600)
boy = load_image('character.png')

clear_canvas()
boy.draw(400, 300)
update_canvas()
delay(1)

def move_circle():
    for degree in range(360):
        theta = math.radians(degree)
        x = 400 + 200 * math.cos(theta)
        y = 300 + 200 * math.sin(theta)

        draw_boy(x,y)
    pass

def move_top():
    for x in range(50, 751, 5):
        draw_boy(x, 550)
        
def move_rectangle():
    move_top()
    move_right()
    move_bottom()
    move_left()
    
    pass

def move_triangle():
    print('triangle')
    pass

def draw_boy(x, y):
    clear_canvas()
    boy.draw(x,y)
    update_canvas()
    delay(0.01)

while True:
    move_circle()
    move_rectangle()
    move_triangle()

    pass

close_canvas()