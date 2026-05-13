from typing import List ,Dict,Any

ONE_PLAYER= 0
PLAYER_TWO= 1


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


def get_input_from_player() -> int:
    user_input = int(input('Select the column you would like to play in'))
    return user_input

def announce_player_turn(current_player: int) -> None:
    print(f"Now it's the turn of: {current_player}")

def print_victory_message(wining_player: int) -> None:
    winning_color = '🔵' if wining_player == ONE_PLAYER else '🔴'
    print(f'The winning player is: {wining_player} / {winning_color}, good for you')

def print_draw_message() -> None:
    print('There is no winner, the result is a draw')

