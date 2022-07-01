# 'A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
# 'A♥', '2♥', '3♥', '4♥', '5♥', '6♥', '7♥', '8♥', '9♥', '10♥', 'J♥', 'Q♥', 'K♥',
# 'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
# 'A♣', '2♣', '3♣', '4♣', '5♣', '6♣', '7♣', '8♣', '9♣', '10♣', 'J♣', 'Q♣', 'K♣'
# playing card unicode: https://en.wikipedia.org/wiki/Playing_cards_in_Unicode
# ♠ = \u2660 , ♥ = \u2665, ♦ \u2666, ♣ \u2663


from turtle import end_fill

suit = "\u2660" , "\u2665", "\u2666", "\u2663"

def get_deck():
    rank = 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'
    # deck = []
    deck = ''
    for i in suit:
        for j in rank:
            # deck.append(j + i)
            deck += j + i + " "
        deck += "\n"
    return deck

def create_deck2():
    rank = list("A23456789") + ["10"] + list("JQK")
    deck = []
    for i in suit:
        for j in rank:
            deck.append(j + i)
    return deck

print(get_deck())
print("-"*100)
print(create_deck2())