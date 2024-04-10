import random

#card number 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    card = random.choice(cards)
    return card

print(card)