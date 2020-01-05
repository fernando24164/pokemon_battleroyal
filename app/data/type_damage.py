import pickle
import logging
from collections import OrderedDict

import pokepy
from beckett.exceptions import InvalidStatusCodeError

logging.basicConfig(level=logging.DEBUG)

client = pokepy.V2Client()


def types_metadata() -> OrderedDict:
    """Generate an ordered dict with all the pokemon types and its metadata

    :return: Dict with all moves with metadata
    :rtype: OrderedDict
    """
    types_complete = OrderedDict()

    n = 1
    while True:
        try:
            response = client.get_type(n)
            types_complete[response.name] = {
                "double_damage_from": [],
                "double_damage_to": [],
                "half_damage_from": [],
                "half_damage_to": [],
                "no_damage_from": [],
                "no_damage_to": [],
            }
            for value in response.damage_relations.double_damage_from:
                types_complete[response.name]["double_damage_from"].append(value.name)
            for value in response.damage_relations.double_damage_to:
                types_complete[response.name]["double_damage_to"].append(value.name)
            for value in response.damage_relations.half_damage_from:
                types_complete[response.name]["half_damage_from"].append(value.name)
            for value in response.damage_relations.half_damage_to:
                types_complete[response.name]["half_damage_to"].append(value.name)
            for value in response.damage_relations.no_damage_from:
                types_complete[response.name]["no_damage_from"].append(value.name)
            for value in response.damage_relations.no_damage_to:
                types_complete[response.name]["no_damage_to"].append(value.name)
            n += 1
        except InvalidStatusCodeError:
            break

    return types_complete


def save_types(types: OrderedDict) -> None:
    """
    Save to pickle file types data

    :param moves: OrderedDict with pokemon data
    :type moves: OrderedDict
    """
    pickle.dump(types, open("./types.pickle", "wb"))


if __name__ == "__main__":
    save_types(types_metadata())
