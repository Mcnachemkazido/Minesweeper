from typing import List ,Dict ,Tuple,Any
from config import NUMBER_PLAYERS


def check_full_column(game_board: List[List[Dict[str,Any]]] ,column_number: int) -> bool:
    return game_board[0][column_number]['is_active']


def check_column_inside_board(game_board: List[List[Dict[str,Any]]], column: int) -> bool:
    return  0 <= column < len(game_board[0])


def fill_first_empty_space_column(game_board: List[List[Dict[str,Any]]],
         column_number: int, type_player: int) -> Tuple[int,int] | None:
    if check_column_inside_board(game_board,column_number) and not check_full_column(game_board, column_number):
            for line in range(len(game_board)-1,-1,-1):
                    if not game_board[line][column_number]['is_active']:
                        game_board[line][column_number]['is_active'] = True
                        game_board[line][column_number]['type_player'] = type_player
                        return line ,column_number
    return None


def switch_turn_between_players(current_player: int) -> int:
    return (current_player + 1) % NUMBER_PLAYERS



