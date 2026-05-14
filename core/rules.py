from typing import List ,Dict ,Tuple,Any
from config import VICTORY_NUMBER


def check_draw(game_board: List[List[Dict[str,Any]]]) -> bool:
    for column in game_board[0]:
        if not column['is_active']:
            return False
    return True


def check_location_within_board_boundaries(game_board: List[List[Dict[str,Any]]],location:Tuple[int,int]) -> bool:
    number_lines = len(game_board)
    number_columns = len(game_board[0])
    return (0 <= location[0] <= number_lines -1) and (0 <= location[1] <= number_columns -1)


def check_direction(location: Tuple[int, int], type_player: int, game_board: List[List[Dict[str, Any]]], step_line: int,
                    step_column: int) -> bool:

    sequence_counter = 1
    line_position = location[0] + step_line
    column_position = location[1] + step_column

    while check_location_within_board_boundaries(game_board, (line_position, column_position)) and \
            game_board[line_position][column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position += step_line
        column_position += step_column

    line_position = location[0] - step_line
    column_position = location[1] - step_column
    while check_location_within_board_boundaries(game_board, (line_position, column_position)) and \
            game_board[line_position][column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position -= step_line
        column_position -= step_column

    return sequence_counter >= VICTORY_NUMBER


def check_win(location: Tuple[int, int], type_player: int, game_board: List[List[Dict[str, Any]]]) -> bool:
    directions = [(0, 1),(1, 0),(1, 1),(1, -1)]
    for step_line, step_column in directions:
        if check_direction(location, type_player, game_board, step_line, step_column):
            return True
    return False


