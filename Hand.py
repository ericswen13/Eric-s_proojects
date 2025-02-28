from Deck import Deck
from Card import Card


class Hand(Deck):
    def __init__(self, name=""):
       self.cards = []
       self.name = name

    def add(self, card):
        self.cards.append(card)

    def __str__(self):
        s = "Hand " + self.name
        if self.is_empty():
            s += " is empty\n"
        else:
            s += " contains\n"
        return s + Deck.__str__(self)
