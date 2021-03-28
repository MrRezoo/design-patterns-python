"""
    Creational :
        Factory
"""


from abc import ABC, abstractmethod
from random import choice


class PlayerBase(ABC):
    choices = ['r', 'p', 's']

    @abstractmethod
    def move(self):
        pass


class HumanPlayer(PlayerBase):
    def move(self):
        mov = input("Chose your next move...")
        return mov


class SystemPlayer(PlayerBase):
    def move(self):
        return choice(self.choices)


class Game:
    @staticmethod
    def start_game():
        game_type = input(
            "Please chose game type(s -> single player , m -> multiple player)")
        if game_type == 's':
            p1 = HumanPlayer()
            p2 = SystemPlayer()
        elif game_type == 's':
            p1 = HumanPlayer()
            p2 = HumanPlayer()
        else:
            print("invalid input")
            p1 = None
            p2 = None
        return p1, p2


if __name__ == '__main__':
    player1, player2 = Game().start_game()

    for player in [player1,player2]:
        player.move()