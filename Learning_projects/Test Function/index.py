import random

#card number 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def card_deal():
    card = random.choice(cards)
    return card

my_card = []
computer_card = []

for _ in range(2):
    my_card.append(card_deal())


print(my_card)

total = 0

for each in my_card:
    total += each

print(total)

def more_card():
    card_decision = input()

    if card_decision == "y":
        for _ in range(1):
            my_card.append(card_deal())
    else:
        for each in my_card:
            total_my_card += each    
    print(my_card)
    return my_card

First_new_card = more_card()
if First_new_card == 11:
    First_new_card = 1

total_my_card = 0
for each in my_card:
    total_my_card += each

print(total_my_card) 

if total_my_card > 21:
    print("you lose")

elif total_my_card <= 20:
    for _ in range(1):
        my_card.append(card_deal())
else:
    print("you have 21")        

print(my_card)
