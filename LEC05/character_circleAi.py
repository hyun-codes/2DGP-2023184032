from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

center_x = 400
center_y = 300

radius = 200
radian = 0.0

game_is_running = True

while game_is_running:

    # 이벤트 처리
    for event in get_events():
        if event.type == SDL_QUIT:
            game_is_running = False

    # 각도 증가
    radian += 0.03

    # 원 위의 현재 좌표 계산
    x = center_x + radius * math.cos(radian)
    y = center_y + radius * math.sin(radian)

    # 화면 그리기
    clear_canvas()

    character.draw(x, y)

    update_canvas()

    delay(0.01)

close_canvas()