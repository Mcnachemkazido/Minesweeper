from typing import List ,Dict ,Tuple,Any

VICTORY_NUMBER = 4

def check_draw(game_board: List[List[Dict[str,Any]]]) -> bool:
    for column in game_board[0]:
        if not column['is_active']:
            return False
    return True


def check_within_board_boundaries(game_board: List[List[Dict[str,Any]]],location:Tuple[int,int]) -> bool:
    number_lines = len(game_board)
    number_columns = len(game_board[0])
    return (0 <= location[0] <= number_lines -1) and (0 <= location[1] <= number_columns -1)


def check_horizontal(location: Tuple[int,int],
                            type_player:int,game_board: List[List[Dict[str,Any]]]) -> bool:

    sequence_counter = 1
    line_position = location[0]
    column_position = location[1] + 1

    while check_within_board_boundaries(game_board ,(line_position,column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        column_position += 1

    line_position = location[0]
    column_position = location[1] -1
    while check_within_board_boundaries(game_board, (line_position, column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        column_position -= 1

    if sequence_counter >= VICTORY_NUMBER:
        return True

    return False



def check_vertical(location: Tuple[int,int],
                            type_player:int,game_board: List[List[Dict[str,Any]]]) -> bool:

    sequence_counter = 1
    line_position = location[0] + 1
    column_position = location[1]

    while check_within_board_boundaries(game_board ,(line_position,column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position += 1

    line_position = location[0] -1
    column_position = location[1]
    while check_within_board_boundaries(game_board, (line_position, column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position -= 1

    if sequence_counter >= VICTORY_NUMBER:
        return True

    return False


def check_descending_diagonal(location: Tuple[int,int],
                            type_player:int,game_board: List[List[Dict[str,Any]]]) -> bool:
    sequence_counter = 1
    line_position = location[0] + 1
    column_position = location[1] + 1

    while check_within_board_boundaries(game_board ,(line_position,column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position += 1
        column_position += 1


    line_position = location[0] -1
    column_position = location[1] -1
    while check_within_board_boundaries(game_board, (line_position, column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position -= 1
        column_position -= 1

    if sequence_counter >= VICTORY_NUMBER:
        return True
    return False




def check_ascending_diagonal(location: Tuple[int,int],
                            type_player:int,game_board: List[List[Dict[str,Any]]]) -> bool:
    sequence_counter = 1
    line_position = location[0] + 1
    column_position = location[1] - 1

    while check_within_board_boundaries(game_board ,(line_position,column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position += 1
        column_position -= 1


    line_position = location[0] -1
    column_position = location[1] +1
    while check_within_board_boundaries(game_board, (line_position, column_position)) and game_board[line_position][
        column_position]['type_player'] == type_player:
        sequence_counter += 1
        line_position -= 1
        column_position += 1

    if sequence_counter >= VICTORY_NUMBER:
        return True

    return False


def check_win(location: Tuple[int,int],
                            type_player:int,game_board: List[List[Dict[str,Any]]]) -> bool:
    return (check_horizontal(location,type_player,game_board) or
            check_vertical(location,type_player,game_board) or
            check_ascending_diagonal(location,type_player,game_board) or
            check_descending_diagonal(location,type_player,game_board))