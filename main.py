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

# possible_cards = []
left_over=[deck.pop(random.randrange(len(deck)))] # Stos kart odrzuconych dobieramy losową kartę na wieszch tak jak w UNO
player_hand_one = [deck.pop(random.randrange(len(deck))) for i in range(6)]+["DOBIERZ"] # Losowe 6 kart na rękę gracza
player_hand_two = [deck.pop(random.randrange(len(deck))) for i in range(6)]+["DOBIERZ"] # Losowe 6 kart na rękę gracza

def player_check(current_player): # Sprawdzanie gracza w celu dobboru ręki gracza
    if current_player == 1:
        return player_hand_one
    else:
        return player_hand_two
class Uno(TwoPlayerGame):
    def __init__(self, players=None):
        self.players = players 
        self.current_player = 2 
        # self.player_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)]+["DOBIERZ"]
        # self.player_two_hand = [deck.pop(random.randrange(len(deck))) for i in range(6)] +["DOBIERZ"]  # 6 cards for start in each player's hand
        # self.opponent = Human_Player()  # Create an opponent player
        self.deck = deck 
    

    def possible_moves(self):       # Sprawdzanie jakie ruchy może wykonać gracz i zwracanie tablicy ruchów (possible_cards)
        possible_cards = []
        current_player_hand = player_check(self.current_player) 

        for i in current_player_hand:
            if i[0].isdigit(): 
                if i[1] == left_over[-1][1]:
                    possible_cards.append(i)
                elif i[0] == left_over[-1][0]:
                    possible_cards.append(i)
            # elif left_over[-1][0] == "+":       # puki co opcja dodawania kart za pomocą +2 albo +4 nie jest zaimplementowana  
            #     if i[2] == left_over[-1][2] or i[1] == "4":
            #         possible_cards.append(i)
            else:
                possible_cards.append("DOBIERZ")   
        return possible_cards

    def make_move(self, move):          #Wykonywanie ruchu
        current_player_hand = player_check(self.current_player) 

        if move[0].isdigit(): #czy karta ma licze
            if left_over[-1][1] == move[1]: # czy kolor się zgadza
                current_player_hand.remove(move) #usuwanie z ręki
                left_over.append(move)  # dodawanie do stosu kart odrzuconych 
        # elif move[0] == "+":   #implementacja kart +2 i +4 powinna działać lecz w pierwszej kolejności podstawy są najważniejsze
        #     if move[1] == "2":
        #         for i in range(2):
        #             current_player_hand.append(deck.pop(random.randrange(len(deck))) )  
        #         current_player_hand.remove(move)
        #         left_over.append(move)
        #     else:
        #         for i in range(4):
        #             current_player_hand.append(deck.pop(random.randrange(len(deck))) )  
        #         current_player_hand.remove(move)
        #         left_over.append(move)
        elif move == "DOBIERZ":     #Dobieranie kart w przypadku braku możliwości zagrania jakiej kolwiek
            current_player_hand.append(deck.pop(random.randrange(len(deck)))) 


    def win(self):
        current_player_hand = player_check(self.current_player) 
        return (len(current_player_hand) <= 1 and current_player_hand[0]=="DOBIERZ")  # Jeśli na ręce pozostaje tylko opcja dobierania wygrywasz
    
    def is_over(self):
        return self.win()

    def scoring(self):
        return 100 if self.win() else 0
    
    def show(self): #Wyświetlanie ręki + dodatkowe informacje przydatne przy testowaniu 
        current_player_hand = player_check(self.current_player) 
        print(f"Player {self.current_player} hand:")
        for x in current_player_hand:
            print(f"[{x}] ", end="")
        print(f"\nLeftOver {left_over}")
        print(f"leftover len:{len(left_over)}")
        print(f"\nTop card {left_over[-1]}")


ai = Negamax(1) # The AI will think 10 moves in advance
game = Uno( [ AI_Player(ai), Human_Player() ] )
history = game.play()