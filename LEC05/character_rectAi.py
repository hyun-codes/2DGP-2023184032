from pico2d import *

open_canvas(800, 600)

character = load_image('character.png')
grass = load_image('grass.png')

# 시작 위치
x = 200
y = 150

# 이동 속도
speed = 2

# 방향 상태
# 0: 위
# 1: 오른쪽
# 2: 아래
# 3: 왼쪽
direction = 0

game_is_running = True

while game_is_running:

    # 1. 이벤트 처리
    for event in get_events():
        if event.type == SDL_QUIT:
            game_is_running = False

    # 2. 위치 업데이트
    if direction == 0:
        y += speed

        if y >= 450:
            y = 450
            direction = 1

    elif direction == 1:
        x += speed

        if x >= 600:
            x = 600
            direction = 2

    elif direction == 2:
        y -= speed

        if y <= 150:
            y = 150
            direction = 3

    elif direction == 3:
        x -= speed

        if x <= 200:
            x = 200
            direction = 0

    # 3. 화면 그리기
    clear_canvas()

    character.draw(x, y)

    update_canvas()

    # 4. 프레임 속도 조절
    delay(0.01)

close_canvas()