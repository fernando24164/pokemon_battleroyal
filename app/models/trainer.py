from dataclasses import dataclass
from collections import deque


@dataclass
class Trainer():
    name = str
    age = int
    pokemon = deque

    def has_poke(self) -> bool:
        for poke in self.pokemon:
            if poke.have_energy():
                return True
        return False

    def _set_squadron(self, poke_list: list) -> None:
        for poke in poke_list:
            poke.load_data()
            self.pokemon.append(poke)
