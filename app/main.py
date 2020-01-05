from models.battle import Battle
from models.trainer import Trainer
from time import sleep

if __name__ == "__main__":
    match = Battle(Trainer, Trainer)
    while match.battle_continue():
        sleep(1)
