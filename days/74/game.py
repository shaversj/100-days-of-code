from dataclasses import dataclass
from dataclasses import field
import random

game = ['Rock', 'Paper', 'Scissors']


def results():
    x = random.choice(game)

    return x


@dataclass
class Player:
    name: str


@dataclass
class Roll(Player):
    roll_result: str = field(default_factory=results)

    def roll_defeat(self):
        """
        Determine which roll defeats self.

        "rock crushes scissors"
        "paper covers rock"
        "scissors cuts paper"
        "If both players choose the same shape, the game is tied and is usually immediately replayed to break the tie."


        rock - [paper]
        scissors - [rock]
        paper - [scissors]
        """

        if self.roll_result == 'Rock':
            return 'Paper'

        elif self.roll_result == 'Paper':
            return 'Scissors'

        elif self.roll_result == 'Scissors':
            return 'Rock'
