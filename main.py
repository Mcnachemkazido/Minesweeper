from core.user_interface import select_new_or_previous_game,print_game_board ,get_input_from_player ,print_victory_message,print_draw_message,announce_player_turn
from core.logic import fill_first_empty_space_column ,switch_turn_between_players
from core.initialization_board import create_game_board
from core.rules import check_draw ,check_win
from storage_manager.storage import get_old_game_state ,save_new_state_in_json ,get_the_latest_game_modes
from config import ONE_PLAYER ,QUEUE_TIME ,EXIT_KAY

def run():
    user_decision = select_new_or_previous_game()
    if user_decision in get_the_latest_game_modes():
        game_board = get_old_game_state(user_decision)
    else:
        game_board = create_game_board()
    current_player =  ONE_PLAYER

    while not check_draw(game_board):
        print_game_board(game_board)
        current_player = switch_turn_between_players(current_player)
        announce_player_turn(current_player)
        current_step = get_input_from_player(QUEUE_TIME)
        if current_step is None:
            continue
        if current_step == EXIT_KAY:
            save_new_state_in_json(game_board)
            break
        current_location = fill_first_empty_space_column(game_board,current_step,current_player)
        if check_win(current_location,current_player,game_board):
            print_victory_message(current_player)
            break
    else:
        print_draw_message()


if __name__ == '__main__':
    run()

