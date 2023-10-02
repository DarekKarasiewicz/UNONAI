import random

from easyAI import TwoPlayerGame, Negamax, Human_Player, AI_Player

deck = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        "Block", "Block", "Block", "Block",
        "Reverse","Reverse","Reverse","Reverse",
        "+2", "+2", "+2", "+2",
        "+4", "+4", "+4", "+4"]

class Uno(TwoPlayerGame):
    def __init__(self):
        self.start_hand = []
        self.start_deck = deck
        self.deck = deck
        self.leftover = []

    def get_cards(self):
        for x in range(6):
            self.start_hand.append(deck.pop(random.randrange(len(deck))))

        
