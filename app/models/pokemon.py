from dataclasses import dataclass


@dataclass
class Pokemon(object):

    name: str
    level: int
    stats: dict
    attacks: dict

    def load_data():
        """
        Load pokemon data from data base
        """
        pass
