from typing import List ,Dict ,Any
from config import NUMBER_LIENS ,NUMBER_COLUMNS



def create_game_board(number_liens: int= NUMBER_LIENS,
        number_columns: int= NUMBER_COLUMNS) -> List[List[Dict[str,Any]]]:
    game_board = []
    for line in range(number_liens):
        line = []
        for column in range(number_columns):
            line.append({'is_active':False,'type_player':None})
        game_board.append(line)
    return game_board






