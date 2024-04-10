import random

#card number 

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


#Create function that deal the cards

def card_deal():
    card = random.choice(cards)
    return card

print(card_deal())
#create card holder for myself and computer 

my_card = []
computer_card = []

#deal cards
for _ in range(2):
    my_card.append(card_deal())
    computer_card.append(card_deal())

print(my_card)
print(computer_card)

# if this one is 21 points on the first place, from my_car -> win (no slipt rule)

#total in hand
total_my_card = 0
for each_card in my_card:
    total_my_card += each_card
print(total_my_card)    

if total_my_card == 21 and len(total_my_card) == 2:
    print("You win")
elif total_my_card < 21:
    print("do you want to withdaw another card? Type Y or N")

draw_decision = input()
if draw_decision == "Y":
    for _ in range(3):
        my_third_card = my_card.append(card_deal())

print(my_card)

