import random

from easyAI import TwoPlayerGame, Negamax, Human_Player, AI_Player

deck = ["0B", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B",
        "0R", "1R", "2R", "3R", "4R", "5R", "6R", "7R", "8R", "9R",
        "0Y", "1Y", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y",
        "0G", "1G", "2G", "3G", "4G", "5G", "6G", "7G", "8G", "9G",
        ]

left_over = [deck.pop(random.randrange(len(deck)))]


def player_move(self, move, player_hand):
    if move[0].isdigit():
        if self.left_over[-1][0] == move[0] or self.left_over[-1][1] == move[1]:
            self.left_over.append(move)
            player_hand.remove(move)
    elif move == "DOBIERZ":
        player_hand.append(deck.pop(random.randrange(len(deck))))


class Uno(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players
        self.current_player = 2
        self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] + ["DOBIERZ"]
        self.player_two_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] + ["DOBIERZ"]
        self.deck = deck
        self.left_over = left_over

    def possible_moves(self):
        possible_cards = []

        if self.current_player == 1:
            for i in self.player_hand:
                if i[0].isdigit():
                    if i[1] == self.left_over[-1][1]:
                        possible_cards.append(i)
                    elif i[0] == self.left_over[-1][0]:
                        possible_cards.append(i)
                else:
                    possible_cards.append("DOBIERZ")
            return possible_cards

        elif self.current_player == 2:
            for i in self.player_two_hand:
                if i[0].isdigit():
                    if i[1] == self.left_over[-1][1]:
                        possible_cards.append(i)
                    elif i[0] == self.left_over[-1][0]:
                        possible_cards.append(i)
                else:
                    possible_cards.append("DOBIERZ")
            return possible_cards

    def make_move(self, move):
        # if self.deck:
        #     self.deck = self.left_over
        #     self.left_over = self.deck.pop(self.deck[-1])

        if self.current_player == 1:
            player_move(self, move, self.player_hand)
        elif self.current_player == 2:
            player_move(self, move, self.player_two_hand)

    def win(self):
        """

        :return:
        """
        return len(self.player_hand) <= 1 or len(self.player_two_hand) <= 1

    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0

    def show(self):
        if self.current_player == 1:
            current_player_hand = self.player_hand
        else:
            current_player_hand = self.player_two_hand
        print(f"Player {self.current_player} hand:")
        for x in current_player_hand:
            print(f"[{x}] ", end="")
        print(f"\nTop card {self.left_over[-1]}")


ai = Negamax(1)
game = Uno([AI_Player(ai), Human_Player()])
history = game.play()
