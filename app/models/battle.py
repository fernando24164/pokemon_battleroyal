from dataclasses import dataclass
from .trainer import Trainer


@dataclass
class Battle:
    trainer: Trainer
    trainer2: Trainer

    def battle_continue(self) -> bool:
        return self.trainer.has_poke() and self.trainer2.has_poke()
