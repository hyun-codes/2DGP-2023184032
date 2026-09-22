from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')
#grass = load_image('grass.png')

radian = 0.0
radius = 200

game_is_running = True

def isCalc(x, y, radian):
    x = x + radius * math.cos(radian)
    y = y + radius * math.sin(radian)
    return x, y

while game_is_running:
    clear_canvas()

    radian += 0.17

    x, y = isCalc(400, 300, radian)

    character.draw(x, y)

    update_canvas()
    delay(0.01)

    for event in get_events():
        if event.type == SDL_QUIT:
            game_is_running = False
            

close_canvas()

