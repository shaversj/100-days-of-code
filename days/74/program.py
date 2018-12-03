from dataclasses import dataclass
import random

game = ['Rock', 'Paper', 'Scissors']


@dataclass
class Player:
    name: str


class Roll(Player):
    roll_result: random.choice(game)

    def determine_which_roll_wins():
        pass

    def determine_which_roll_defeats_self():
        pass
