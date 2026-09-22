from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')
grass = load_image('grass.png')

#시작 점.
x = 200
y = 150

game_is_running = True

while game_is_running:
    

    while y < 450 and game_is_running:
        for event in get_events():
                    if event.type == SDL_QUIT:
                        game_is_running = False

        clear_canvas()
        character.draw(x, y)
        y +=2
        update_canvas()
        delay(0.01)

    while x < 600 and game_is_running:
        for event in get_events():
                    if event.type == SDL_QUIT:
                        game_is_running = False

        clear_canvas()
        character.draw(x,y)
        x +=2
        update_canvas()
        delay(0.01)

    while y > 150 and game_is_running:
        for event in get_events():
                    if event.type == SDL_QUIT:
                        game_is_running = False

        clear_canvas()
        character.draw(x,y)
        y-=2
        update_canvas()
        delay(0.01)

    while x > 200 and game_is_running:
        for event in get_events():
                    if event.type == SDL_QUIT:
                        game_is_running = False
                        
        clear_canvas()
        character.draw(x,y)
        x -=2
        update_canvas()
        delay(0.01)

    

close_canvas()

