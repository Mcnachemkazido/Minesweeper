import json
import os
from config import STORAGE_PATH


def write_to_json_file(data,file_name: str = STORAGE_PATH) -> None:
    with open(file_name, "w") as file:
        json.dump(data, file)


def load_json_file(file_name: str = STORAGE_PATH):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            loaded_data = json.load(file)
            return loaded_data
    else:
        return {}

def get_the_latest_games_situations():
    state_json = load_json_file()
    return [i for i in state_json.keys()]


def save_new_state_in_json(game_state):
    state_json = load_json_file()
    state_json[len(state_json) + 1] = game_state
    write_to_json_file(state_json)


def get_specific_old_game_state(game_state: str):
    if game_state in get_the_latest_games_situations():
        return load_json_file()[game_state]
    return None
