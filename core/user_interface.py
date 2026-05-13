import keyboard
from threading import Timer
from typing import List ,Dict,Any
from config import ONE_PLAYER ,PLAYER_TWO ,EXIT_KAY


def print_game_board(game_board: List[List[Dict[str,Any]]]) -> None:
    for line in game_board:
        for column in line:
            if column['type_player'] == ONE_PLAYER:
                print('🔵',end='|')
            elif column['type_player'] == PLAYER_TWO:
                print('🔴',end='|')
            else:
                print('  ',end='|')

        print()



def get_input_from_player(input_time: int):
    t = Timer(input_time, lambda: print("\nyour writing time is over!!\npress ENTER to continue the game"))
    t.start()

    print(f"you have {input_time} seconds to select the column you would like to play in")
    while True:
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            answer = event.name
            break
    t.cancel()

    if answer == EXIT_KAY:
        return EXIT_KAY
    elif answer == 'enter':
        return None
    try:
        return int(answer)
    except ValueError:
        return None

def select_new_or_previous_game():
    user_decision = input('If you want to play an old game,\nenter its serial number, if not, enter new')
    return user_decision


def announce_player_turn(current_player: int) -> None:
    print(f"Now it's the turn of: {current_player}")

def print_victory_message(wining_player: int) -> None:
    winning_color = '🔵' if wining_player == ONE_PLAYER else '🔴'
    print(f'The winning player is: {wining_player} / {winning_color}, good for you')

def print_draw_message() -> None:
    print('There is no winner, the result is a draw')

