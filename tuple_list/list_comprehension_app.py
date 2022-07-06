"""
    'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
    'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
    'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
    'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
    """
import random


rank = list("A23456789") + ["10"] + list("JQK")
suit = ("\u2660", "\u2665", "\u2666", "\u2663") # https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
     
def deck_create():
    deck = []
    
    for r in rank:
        for s in suit:
            x = r+s
            deck.append(r+s)
            
    return deck     

# using list comprehension
def deck_create2():
    # return [ r+s for r in rank for s in suit]
    return [ (r,s) for r in rank for s in suit ]

# print(deck_create())
# print(deck_create2())

d = deck_create()
# random.shuffle(d)
print(d)
print(random.choice(d))