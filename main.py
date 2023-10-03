import random

from easyAI import TwoPlayerGame, Negamax, Human_Player, AI_Player

deck = ["0B", "1B", "2B", "3B", "4B", "5B", "6B", "7B", "8B", "9B",
        "0R", "1R", "2R", "3R", "4R", "5R", "6R", "7R", "8R", "9R",
        "0Y", "1Y", "2Y", "3Y", "4Y", "5Y", "6Y", "7Y", "8Y", "9Y",
        "0G", "1G", "2G", "3G", "4G", "5G", "6G", "7G", "8G", "9G",
        # "BG", "BB", "BY", "BR",
        # "RG","RB","RY","RR",
        # "+2B", "+2G", "+2Y", "+2R",
        # "+4", "+4", "+4", "+4"
        ]

possible_cards = []
left_over=[deck.pop(random.randrange(len(deck)))]
class Uno(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players 
        self.current_player = 2 # player 1 start
        self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)]+["DOBIERZ"]
        self.player_two_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] +["DOBIERZ"]  # 6 cards for start in each player's hand
        # self.opponent = Human_Player()  # Create an opponent player
        self.deck = deck

    def get_card(self):
        self.player_hand.append(deck.pop(random.randrange(len(deck)))) 
    
    def get_two_or_four_cards(self,card,hand):
        if card[1] == "2" :
            for i in range(2):
                hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand  
        # elif card == "+4" :
        #     for i in range(4):
        #         hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand 

    def possible_moves(self):
        possible_cards = []
        if self.current_player == 1:
            for i in self.player_hand:
                if i[0].isdigit(): #musi być ostatnia oki

                    if i[1] == left_over[-1][1]:
                        possible_cards.append(i)
                    elif i[0] == left_over[-1][0]:
                        possible_cards.append(i)

                elif left_over[-1][0] == "+": #to zadziała ?? Jest taka szansa ale nie wiem czy to tak nie będzię wyglądać [1,2]
                    if i[2] == left_over[-1][2] or i[1] == "4":
                        possible_cards.append(i)
                else:
                    possible_cards.append("DOBIERZ")   
            return possible_cards
        elif self.current_player == 2:
            for i in self.player_two_hand:
                if i[0].isdigit(): #musi być ostatnia oki

                    if i[1] == left_over[-1][1]:
                        possible_cards.append(i)
                    elif i[0] == left_over[-1][0]:
                        possible_cards.append(i)

                elif left_over[-1][0] == "+": #to zadziała ?? Jest taka szansa ale nie wiem czy to tak nie będzię wyglądać [1,2]
                    if i[2] == left_over[-1][2] or i[1] == "4":
                        possible_cards.append(i)
                else:
                    possible_cards.append("DOBIERZ")   
            return possible_cards

    def make_move(self, move):
        if self.current_player == 1:
            if move[0].isdigit():
                if left_over[-1][1] == move[1]:
                    self.player_hand.remove(move) 
                    left_over.append(move)
            elif move[0] == "+":
                if move[1] == "2":
                    for i in range(2):
                        self.player_hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand  
                    self.player_hand.remove(move)
                    left_over.append(move)
                else:
                    for i in range(4):
                        self.player_hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand  
                    self.player_hand.remove(move)
                    left_over.append(move)
            elif move == "DOBIERZ":
                self.player_hand.append(deck.pop(random.randrange(len(deck)))) 

        elif self.current_player == 2:
            if move[0].isdigit():
                if left_over[-1][1] == move[1]:
                    self.player_two_hand.remove(move) 
                    left_over.append(move)
            elif move[0] == "+":
                if move[1] == "2":
                    for i in range(2):
                        self.player_two_hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand  
                    self.player_two_hand.remove(move)
                    left_over.append(move)
                else:
                    for i in range(4):
                        self.player_two_hand.append(deck.pop(random.randrange(len(deck))) )  # 6 card for start in each player hand  
                    self.player_two_hand.remove(move)
                    left_over.append(move)
            elif move == "DOBIERZ":
                self.player_two_hand.append(deck.pop(random.randrange(len(deck)))) 



    def win(self):
        return (len(self.player_hand) <= 1 and self.player_hand[0]=="DOBIERZ") or (len(self.player_two_hand) <= 1 and self.player_hand[0]=="DOBIERZ")
    
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
        print(f"\nTop card {left_over[-1]}")


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

