import pickle
import logging
from time import sleep
from collections import OrderedDict

import pokepy


logging.basicConfig(level=logging.DEBUG)


client = pokepy.V2Client()
pokedex = OrderedDict()


for poke_index in range(152):
    try:
        poke = client.get_pokemon(poke_index)
        pokedex[poke.name] = {"moves": [], "stats": [], "type": []}
        for stats in poke.stats:
            response = {}
            response["name"] = stats.stat.name
            response["value"] = stats.base_stat
            pokedex[poke.name]["stats"].append(response)
        for move in poke.moves:
            pokedex[poke.name]["moves"].append(move.move.name)
        for types in poke.types:
            pokedex[poke.name]["type"].append(types.type.name)
        logging.debug(pokedex[poke.name])
        sleep(2)
    except Exception as e:
        logging.debug("Exception %s" % e)

pickle.dump(pokedex, open("./pokedex.pickle", "wb"))
