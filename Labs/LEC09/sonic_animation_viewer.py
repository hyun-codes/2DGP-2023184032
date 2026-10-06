"""소닉 스프라이트 시트의 애니메이션을 순서대로 보여 준다."""

from pico2d import *

CANVAS_WIDTH = 1200
CANVAS_HEIGHT = 800
SPRITE_SHEET_WIDTH = 399
SPRITE_SHEET_HEIGHT = 525
FRAME_INTERVAL = 0.1
ACTION_REPEAT_COUNT = 5
ACTION_PAUSE_SECONDS = 1.0
DEFAULT_SCALE = 4
CANVAS_MARGIN = 40
IMAGE_PATH = 'sonic-sprite.png'
PLAYING = 'playing'
PAUSED_BETWEEN_ACTIONS = 'paused_between_actions'
MOVEMENT_CENTER = 'center'
MOVEMENT_HORIZONTAL = 'horizontal'
MOVEMENT_VERTICAL = 'vertical'

# 프레임 좌표 형식: (왼쪽 x, 아래쪽 y, 너비, 높이)
ACTIONS = (
    {
        'name': '대기와 웅크리기',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
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
        'name': '걷기와 달리기',
        'movement': MOVEMENT_HORIZONTAL,
        'speed': 120.0,
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
    {
        'name': '발차기',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
        'frames': (
            (1, 361, 33, 40),
            (39, 362, 35, 39),
            (89, 362, 35, 38),
            (130, 362, 34, 42),
            (181, 362, 34, 41),
            (228, 363, 33, 40),
        ),
    },
    {
        'name': '회전 진입',
        'movement': MOVEMENT_HORIZONTAL,
        'speed': 220.0,
        'frames': (
            (1, 326, 29, 30),
            (36, 327, 28, 31),
            (67, 327, 30, 29),
            (98, 327, 31, 28),
            (131, 327, 29, 30),
            (162, 326, 29, 31),
            (193, 326, 30, 29),
            (230, 327, 31, 28),
            (268, 325, 30, 30),
        ),
    },
    {
        'name': '회전 구르기',
        'movement': MOVEMENT_HORIZONTAL,
        'speed': 220.0,
        'frames': (
            (1, 292, 30, 27),
            (36, 292, 29, 27),
            (70, 292, 29, 27),
            (105, 292, 29, 27),
            (139, 292, 29, 27),
            (174, 292, 29, 27),
        ),
    },
    {
        'name': '수직 점프',
        'movement': MOVEMENT_VERTICAL,
        'speed': 0.0,
        'jump_height': 220.0,
        'frames': (
            (1, 251, 29, 35),
            (36, 251, 30, 35),
            (74, 251, 31, 35),
            (111, 251, 31, 36),
            (149, 251, 30, 35),
            (186, 251, 31, 36),
        ),
    },
    {
        'name': '특수 동작',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
        'frames': (
            (1, 207, 29, 35),
            (36, 207, 30, 35),
            (72, 208, 39, 31),
            (123, 208, 39, 32),
            (172, 208, 39, 31),
            (218, 208, 38, 32),
        ),
    },
    {
        'name': '피격과 쓰러짐',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
        'frames': (
            (1, 154, 24, 45),
            (31, 154, 29, 44),
            (65, 154, 20, 44),
            (90, 155, 25, 43),
            (119, 155, 25, 43),
            (149, 154, 20, 44),
            (184, 156, 40, 28),
            (232, 157, 39, 27),
        ),
    },
    {
        'name': '균형 잡기와 밀기',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
        'frames': (
            (1, 108, 27, 38),
            (31, 110, 31, 36),
            (64, 110, 31, 36),
            (99, 110, 33, 38),
            (136, 110, 32, 36),
            (176, 110, 33, 36),
            (217, 110, 33, 36),
            (254, 111, 33, 36),
        ),
    },
    {
        'name': '위아래 보기',
        'movement': MOVEMENT_CENTER,
        'speed': 0.0,
        'frames': (
            (6, 56, 34, 40),
            (49, 56, 34, 43),
            (96, 59, 23, 39),
            (125, 59, 23, 39),
        ),
    },
)


def get_frame_scale(frame):
    _, _, width, height = frame
    return min(DEFAULT_SCALE,
               (CANVAS_WIDTH - CANVAS_MARGIN * 2) / width,
               (CANVAS_HEIGHT - CANVAS_MARGIN * 2) / height)


def draw_frame(sprite_sheet, frame, destination_x, destination_y, direction):
    x, y, width, height = frame
    scale = get_frame_scale(frame)
    draw_width = width * scale
    draw_height = height * scale
    if direction < 0:
        sprite_sheet.clip_composite_draw(
            x, y, width, height, 0, 'h',
            destination_x, destination_y, draw_width, draw_height)
    else:
        sprite_sheet.clip_draw(
            x, y, width, height,
            destination_x, destination_y, draw_width, draw_height)


def get_action_horizontal_bounds(action):
    half_width = max(
        frame[2] * get_frame_scale(frame) / 2
        for frame in action['frames']
    )
    return (CANVAS_MARGIN + half_width,
            CANVAS_WIDTH - CANVAS_MARGIN - half_width)


def get_initial_position(action):
    if action['movement'] != MOVEMENT_HORIZONTAL:
        return CANVAS_WIDTH / 2, CANVAS_HEIGHT / 2
    left_bound, _ = get_action_horizontal_bounds(action)
    return left_bound, CANVAS_HEIGHT / 2


def update_horizontal_position(action, position_x, direction, elapsed_time):
    if action['movement'] != MOVEMENT_HORIZONTAL:
        return position_x, direction

    left_bound, right_bound = get_action_horizontal_bounds(action)
    position_x += action['speed'] * direction * elapsed_time
    while position_x < left_bound or position_x > right_bound:
        if position_x > right_bound:
            position_x = right_bound - (position_x - right_bound)
            direction = -1
        elif position_x < left_bound:
            position_x = left_bound + (left_bound - position_x)
            direction = 1
    return position_x, direction


def get_vertical_position(action, action_elapsed):
    if action['movement'] != MOVEMENT_VERTICAL:
        return CANVAS_HEIGHT / 2

    jump_duration = len(action['frames']) * FRAME_INTERVAL
    jump_phase = (action_elapsed % jump_duration) / jump_duration
    jump_offset = 4 * action['jump_height'] * jump_phase * (1 - jump_phase)
    return CANVAS_HEIGHT / 2 + jump_offset


def handle_events():
    for event in get_events():
        if event.type == SDL_QUIT:
            return False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            return False
    return True


def get_next_action_index(action_index):
    """마지막 동작 다음에는 첫 번째 동작을 선택한다."""
    return (action_index + 1) % len(ACTIONS)


def validate_actions():
    """동작 이름과 모든 프레임 좌표가 유효한지 확인한다."""
    if not ACTIONS:
        raise ValueError('재생할 소닉 동작이 없습니다.')

    action_names = set()
    horizontal_action_count = 0
    vertical_action_count = 0
    centered_action_count = 0
    for action in ACTIONS:
        name = action['name']
        frames = action['frames']
        movement = action['movement']
        speed = action['speed']
        if not name or name in action_names:
            raise ValueError(f'동작 이름이 비어 있거나 중복되었습니다: {name!r}')
        if not frames:
            raise ValueError(f'{name} 동작에 프레임이 없습니다.')
        if movement not in (MOVEMENT_CENTER,
                            MOVEMENT_HORIZONTAL,
                            MOVEMENT_VERTICAL):
            raise ValueError(f'{name} 동작의 이동 유형이 잘못되었습니다.')
        if speed < 0 or (movement == MOVEMENT_HORIZONTAL and speed == 0):
            raise ValueError(f'{name} 동작의 이동 속도가 잘못되었습니다.')
        if movement != MOVEMENT_HORIZONTAL and speed != 0:
            raise ValueError(f'{name} 동작에는 수평 이동 속도를 사용할 수 없습니다.')
        if movement == MOVEMENT_VERTICAL and action.get('jump_height', 0) <= 0:
            raise ValueError(f'{name} 동작의 점프 높이가 잘못되었습니다.')
        if movement == MOVEMENT_CENTER:
            centered_action_count += 1
        elif movement == MOVEMENT_HORIZONTAL:
            horizontal_action_count += 1
        else:
            vertical_action_count += 1
        action_names.add(name)

        for x, y, width, height in frames:
            if (x < 0 or y < 0 or width <= 0 or height <= 0 or
                    x + width > SPRITE_SHEET_WIDTH or
                    y + height > SPRITE_SHEET_HEIGHT):
                raise ValueError(f'{name} 동작의 프레임 범위가 잘못되었습니다.')

    if (horizontal_action_count != 3 or
            vertical_action_count != 1 or
            centered_action_count != 6):
        raise ValueError('수평 이동 3종, 수직 이동 1종, 제자리 6종이 필요합니다.')


def main():
    validate_actions()
    open_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    try:
        sprite_sheet = load_image(IMAGE_PATH)

        action_index = 0
        current_action = ACTIONS[action_index]
        frames = current_action['frames']
        frame_index = 0
        completed_repeats = 0
        playback_state = PLAYING
        last_frame_time = get_time()
        last_position_time = last_frame_time
        pause_started_at = None
        position_x, position_y = get_initial_position(current_action)
        direction = 1
        action_elapsed = 0.0
        running = True
        while running:
            current_time = get_time()
            elapsed_time = current_time - last_position_time
            if playback_state == PLAYING:
                action_elapsed += elapsed_time
                position_x, direction = update_horizontal_position(
                    current_action, position_x, direction, elapsed_time)
                position_y = get_vertical_position(
                    current_action, action_elapsed)
            last_position_time = current_time

            if (playback_state == PLAYING and
                    current_time - last_frame_time >= FRAME_INTERVAL):
                next_frame_index = (frame_index + 1) % len(frames)
                if next_frame_index == 0:
                    completed_repeats += 1
                    if completed_repeats >= ACTION_REPEAT_COUNT:
                        playback_state = PAUSED_BETWEEN_ACTIONS
                        frame_index = len(frames) - 1
                        pause_started_at = current_time
                        if current_action['movement'] == MOVEMENT_VERTICAL:
                            position_y = CANVAS_HEIGHT / 2
                    else:
                        frame_index = next_frame_index
                else:
                    frame_index = next_frame_index
                last_frame_time = current_time
            elif (playback_state == PAUSED_BETWEEN_ACTIONS and
                  current_time - pause_started_at >= ACTION_PAUSE_SECONDS):
                action_index = get_next_action_index(action_index)
                current_action = ACTIONS[action_index]
                frames = current_action['frames']
                playback_state = PLAYING
                frame_index = 0
                completed_repeats = 0
                last_frame_time = current_time
                last_position_time = current_time
                pause_started_at = None
                position_x, position_y = get_initial_position(current_action)
                direction = 1
                action_elapsed = 0.0

            clear_canvas()
            draw_frame(sprite_sheet, frames[frame_index],
                       position_x, position_y, direction)
            update_canvas()

            running = handle_events()
            delay(0.001)
    finally:
        close_canvas()


if __name__ == '__main__':
    main()
