import pickle
import logging
from pathlib import Path
from collections import OrderedDict

import pokepy

logging.basicConfig(level=logging.DEBUG)


def get_moves() -> list:
    """
    Get unique moves from pokemons

    :return: List with unique pokemons movement
    :rtype: list
    """
    project_dirname = Path.cwd()

    pokedex = pickle.load(file=open(str(project_dirname) + "/pokedex.pickle", "rb"))

    moves_arr = []

    def check_moves(moves):
        def check_poke(moves):
            for move in moves:
                if move not in moves_arr:
                    moves_arr.append(move)

        return check_poke(moves)

    for poke in pokedex.values():
        check_moves(poke["moves"])

    return moves_arr


def complete_pokemon_movement_data(moves: list) -> OrderedDict:
    """
    Get more data from movement

    :param moves: movements list
    :type moves: list
    :return: Dictionary with power pp and more data
    :rtype: OrderedDict
    """
    client = pokepy.V2Client()
    moves_complete = OrderedDict()

    for move in moves:
        moves_complete[move] = {"pp": 0, "power": 0, "accuracy": 0, 'type': ''}
        response = client.get_move(move)
        moves_complete[move]["accuracy"] = response.accuracy
        moves_complete[move]["power"] = response.power
        moves_complete[move]["pp"] = response.pp
        moves_complete[move]["type"] = response.type.name

    return moves_complete


def save_moves(moves: OrderedDict) -> None:
    """
    Save to pickle file movement data

    :param moves: OrderedDict with pokemon data
    :type moves: OrderedDict
    """
    pickle.dump(moves, open("./movement.pickle", "wb"))


if __name__ == "__main__":
    save_moves(complete_pokemon_movement_data(get_moves()))
