import json
import os
from config import STORAGE_PASS


def write_to_json_file(data,file_name: str = STORAGE_PASS) -> None:
    with open(file_name, "w") as file:
        json.dump(data, file)


def load_json_file(file_name: str = STORAGE_PASS):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            loaded_data = json.load(file)
            return loaded_data
    else:
        return {}

def get_the_latest_game_modes():
    state_json = load_json_file()
    return [i for i in state_json.keys()]


def save_new_state_in_json(game_state):
    state_json = load_json_file()
    state_json[len(state_json) + 1] = game_state
    write_to_json_file(state_json)


def get_old_game_state(game_state: str):
    if game_state in get_the_latest_game_modes():
        return load_json_file()[game_state]
    return None
