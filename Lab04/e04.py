import random

class Player:
    def __init__(self, name):
        self.name = name
        self.throw_value = 1

    def validate_throw(self):
        if self.throw_value <= 0 or self.throw_value > 6:
            print("Throw is out of range")

    def throw_die(self):
        self.throw_value = random.randint(1, 6)
        self.validate_throw()


class DiceGame:
    def __init__(self, players):
        self.players = players
        self.rounds = 0
        self.scores = dict()

    def round(self):
        self.rounds += 1
        for player in self.players:
            player.throw_die()
            self.scores.update({player.name: player.throw_value})

    def build_scores(self):
        for player in self.players:
            self.scores.update({player.name: 0})

    def print_scores(self):
        for name, score in self.scores.items():
            print(name, score)

    def winner(self):
        highest_score = 0
        winner = list()

        for player in self.players:
            if player.name == self.scores[player.name]:
                if player.throw_value > highest_score:
                    highest_score = player.throw_value

        for player in self.players:
            if player.throw_value == highest_score:
                winner.append(player)

        print("Winner: {}".format(winner))

Nicu = Player("Nicu")
Alex = Player("Alex")
Vlad = Player("Vlad")

player_list = [Nicu, Alex, Vlad]
Dice_game = DiceGame(player_list)

Dice_game.build_scores()
Dice_game.print_scores()

Dice_game.round()
Dice_game.print_scores()

Dice_game.winner()