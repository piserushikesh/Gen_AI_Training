import random
from Card import Card
from Global_Variables import *

class Deck:

    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)


    def shuffle(self):

        random.shuffle(self.all_cards)


    def deal_one(self):
        return self.all_cards.pop()