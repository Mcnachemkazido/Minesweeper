from typing import List ,Dict ,Any
from config import NUMBER_LINES,NUMBER_COLUMNS



def create_game_board(number_lines : int= NUMBER_LINES,
        number_columns: int= NUMBER_COLUMNS) -> List[List[Dict[str,Any]]]:
    game_board = []
    for _ in range(number_lines):
        new_line = []
        for column in range(number_columns):
           new_line.append({'is_active':False,'type_player':None})
        game_board.append(new_line)
    return game_board






