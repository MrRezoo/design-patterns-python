import random


class User:
    pass


class Dice:
    @staticmethod
    def roll():
        return random.randint(1, 6)


class Game:
    def __init__(self, u1, u2):
        self.user1 = u1
        self.user2 = u2
        self.turn = u1
        self.dice = Dice

    def change_turn(self):
        self.turn = self.user2 if self.turn == self.user1 else self.user1


def check_turn_and_roll_dice(game, user):
    if game.turn == user:
        game.change_turn()
        return game.dice.roll()
    return "It's not your turn"


if __name__ == '__main__':
    user1 = User()
    user2 = User()

    game = Game(user1, user2)

    # print(game.roll_dice(user1))
    print(check_turn_and_roll_dice(game,user2))
    print(check_turn_and_roll_dice(game,user1))
    print(check_turn_and_roll_dice(game,user2))
    print(check_turn_and_roll_dice(game,user2))
    print(check_turn_and_roll_dice(game,user1))
    print(check_turn_and_roll_dice(game,user1))
    print(check_turn_and_roll_dice(game,user1))
    print(check_turn_and_roll_dice(game,user2))
    print(check_turn_and_roll_dice(game,user1))
    print(check_turn_and_roll_dice(game,user2))

