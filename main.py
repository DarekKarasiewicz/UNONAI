import random

from easyAI import TwoPlayerGame, Negamax, Human_Player, AI_Player

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        # "Block", "Block", "Block", "Block",
        # "Reverse","Reverse","Reverse","Reverse",
        # "+2", "+2", "+2", "+2",
        # "+4", "+4", "+4", "+4"
        ]

class Uno(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players 
        self.current_player = 2 # player 1 start
        self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)]
        self.player_two_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)]   # 6 cards for start in each player's hand
        # self.opponent = Human_Player()  # Create an opponent player
        self.deck = deck
        self.leftover = [deck.pop(random.randrange(len(deck)))]

    def get_card(self):
        self.player_hand.append(deck.pop(random.randrange(len(deck)))) 
    
    # def get_two_or_four_cards(self,card):
    #     if card == "+2" :
    #         self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(2)]  # 6 card for start in each player hand  
    #     elif card == "+4" :
    #         self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(4)]  # 6 card for start in each player hand  

    def possible_moves(self):
        if self.current_player == 1:
            return self.player_hand
        elif self.current_player == 2:
            return self.player_two_hand

    def make_move(self, move):
        if self.current_player == 1:
            self.player_hand.remove(move)  # remove bones.
        elif self.current_player == 2:
           self.player_two_hand.remove(move) 

        self.leftover.append(move)


    def win(self):
        return len(self.player_hand) <= 0 or len(self.player_two_hand) <= 0
    
    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0
    
    def show(self):
        if self.current_player == 1:
            print("Computer hand:")
            for x in self.player_hand:
                print(f"[{x}] ", end="")
        elif self.current_player == 2:
            print("Your hand:")
            for x in self.player_two_hand:
                print(f"[{x}] ", end="")
        print(f"\nTop card {self.leftover[-1]}")


ai = Negamax(2) # The AI will think 10 moves in advance
game = Uno( [ AI_Player(ai), Human_Player() ] )
history = game.play()

    # def __init__(self, players=None):
    #     self.players = players
    #     self.pile = 20  # start with 20 bones in the pile
    #     self.current_player = 1  # player 1 starts

    # def possible_moves(self):
    #     return ["1", "2", "3", "-1"]

    # def make_move(self, move):
    #     self.pile -= int(move)  # remove bones.

    # def win(self):
    #     return self.pile <= 0  # opponent took the last bone ?

    # def is_over(self):
    #     return self.win()  # game stops when someone wins.

    # def scoring(self):
    #     return 100 if self.win() else 0

    # def show(self):
    #     print("%d bones left in the pile" % (self.pile))

