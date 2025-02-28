#week 3 main
from Card import Card
from Deck import Deck
from Hand import Hand
from OldMaidHand import OldMaidHand 

deck1 = Deck()
deck1.shuffle()
hand1 = Hand("frank")
hand2 = Hand("Emily")
deck1.deal([hand1, hand2], 10)
print(hand1)
print(hand2)

#game = CardGame()
hand3 = OldMaidHand("Jay")
deck1.deal([hand3], 13)
print(hand3)
