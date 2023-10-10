import random

from easyAI import TwoPlayerGame, Negamax, Human_Player, AI_Player

"""
Game rules:

1. Each player draws 6 cards from the deck.
2. At the beginning of the game, a starting card is drawn from the deck.
3. To place a card in the pile, it must match the suit or penalty number at the top of the pile or the starting card.
4. If we do not have a matching card, we must draw a card from the deck.
5. The first player to get rid of all the cards in their hand wins.

Authors : Dariusz Karasiewicz Mikołaj Kusiński
"""

deck = ["0B", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B",
        "0R", "1R", "2R", "3R", "4R", "5R", "6R", "7R", "8R", "9R",
        "0Y", "1Y", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y",
        "0G", "1G", "2G", "3G", "4G", "5G", "6G", "7G", "8G", "9G",
        ]

left_over = [deck.pop(random.randrange(len(deck)))]


def player_move(self, move, player_hand):
    """Ruch gracza
    Function gets played card and list of cards in player hand. On that data analyze what to do next.
    # Ta funkcja pobiera zagraną kartę oraz listę kart w ręce i na podstawie zagranej karty wykonuje ruch.

    :param self:
        all needed data form class
    :param move: String
        Played card
    :param player_hand: String: list
        List of card in player hand
    """
    if move[0].isdigit():
        if self.left_over[-1][0] == move[0] or self.left_over[-1][1] == move[1]:
            self.left_over.append(move)
            player_hand.remove(move)
    elif move == "DOBIERZ":
        if len(self.deck) == 0:
            self.deck = self.left_over
            self.left_over = []
            self.left_over = [self.deck.pop(-1)]
        player_hand.append(self.deck.pop(random.randrange(len(self.deck))))


class Uno(TwoPlayerGame):
    def __init__(self, players=None):
        """
        Constructor of Uno class. initialize fields:
            -current_player: What player start game
            -player_hand = First player list of card in hand
            -player_two_hand = Second player list of card in hand
            -deck = list of cards in game
            -left_over = list of played cards

        """
        self.players = players
        self.current_player = 2
        self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] + ["DOBIERZ"]
        self.player_two_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] + ["DOBIERZ"]
        self.deck = deck
        self.left_over = left_over

    def possible_moves(self):
        """
        All possible moves that player can do

        Function check all cards in player hand if they can be played add to list which return on the end.

        :return:
        String : list
            List of cards that can be played
        """
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
        """
        Make move

        Function gets played card and do player_move

        :param move: String
            Played card.
        """

        if self.current_player == 1:
            player_move(self, move, self.player_hand)
        elif self.current_player == 2:
            player_move(self, move, self.player_two_hand)

    def win(self):
        """Sprawdź czy gracz wygrał
        Check if player win

        This function verifies whether the player has met the winning conditions.

        :return:
        Boolean
            True: if player win .
            False: if player don't win.
        """
        return len(self.player_hand) <= 1 or len(self.player_two_hand) <= 1

    def is_over(self):
        """
        Games end

        If player win end game

        :return:
        Boolean
            True: if player win
            False: if don't
        """
        return self.win()

    def scoring(self):
        """
        Score player move

        Function to score player move, if move win game give score to player

        :return:
        int
            Points after move
        """
        return 100 if self.win() else 0

    def show(self):
        """
        Show output

        Function to show needed information about game like player hand, top left over card.
        """
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
