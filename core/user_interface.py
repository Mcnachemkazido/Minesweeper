import keyboard
import time
from typing import List ,Dict,Any
from config import PLAYER_ONE ,PLAYER_TWO ,COLOR_PLAYER_ONE,COLOR_PLAYER_TWO,EXIT_KEY


def print_game_board(game_board: List[List[Dict[str,Any]]]) -> None:
    for line in game_board:
        print('|', end='')
        for column in line:
            if column['type_player'] == PLAYER_ONE:
                print(COLOR_PLAYER_ONE,end='|')
            elif column['type_player'] == PLAYER_TWO:
                print(COLOR_PLAYER_TWO,end='|')
            else:
                print('  ',end='|')
        print()


def accept_choice_from_user_new_or_previous_game() -> str:
    game_type = input('If you want to play an old game,\nenter its serial number, if not, enter new')
    return  game_type


def announce_player_turn(current_player: int) -> None:
    player_color = COLOR_PLAYER_ONE if current_player == PLAYER_ONE else COLOR_PLAYER_TWO
    print(f"Now it's the turn of: {current_player} / {player_color}")


def print_victory_message(wining_player: int) -> None:
    winning_color = COLOR_PLAYER_ONE if wining_player == PLAYER_ONE else COLOR_PLAYER_TWO
    print(f'The winning player is: {wining_player} / {winning_color}, good for you')


def print_draw_message() -> None:
    print('There is no winner, the result is a draw')


def get_key_with_timer(input_time: int) -> str|None:
    print(f'You have {input_time} seconds to select the column you would like to play in')
    pressed_key = None

    def catch_key(event):
        nonlocal pressed_key
        if event.event_type == keyboard.KEY_DOWN:
            pressed_key = event.name

    hook_handle = keyboard.hook(catch_key)
    start_time = time.time()
    while (time.time() - start_time) < input_time:
        if pressed_key is not None:
            break
    keyboard.unhook(hook_handle)
    return pressed_key


def process_player_input(pressed_key: str | None) -> int|str|None:
    if pressed_key is None:
        return None
    if pressed_key == EXIT_KEY:
        return EXIT_KEY
    if pressed_key.isdigit():
        return int(pressed_key)
    return None


def get_input_from_player(input_time: int) -> int|None|str:
    key = get_key_with_timer(input_time)
    return process_player_input(key)



