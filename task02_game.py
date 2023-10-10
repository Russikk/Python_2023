


""" Гра 21
Грають два гравця, на початку гри гравцям видається по 2 карти 
(на екран виводяться ці карти, + виводяться карти що лишилися в колоді, для перевірки коду)
Потім запитують першого гравця чи хоче він взяти ще одну карту, якщо він відмовився - запитують в другого
Перемагає той хто збере найближчу суму карт до 21, але не більше.

"""


import random

deck_of_cards = [2,  3,  4,  6, 7, 8,  9,  10, 11] * 4

random.shuffle(deck_of_cards)
print(deck_of_cards)

player_1_cards = deck_of_cards[:2]
player_2_cards = deck_of_cards[2:4]


print('Карти грявця 1: ', player_1_cards)
print('Карти грявця 2: ', deck_of_cards[2:4])

del deck_of_cards[0:4]
print(deck_of_cards)


player_1game = int (input('Введіть будь яке число крім 0, якщо хочете взяти ще карту: '))

while (player_1game != 0):
     card1 = deck_of_cards[0]
     print('Ваша карта: ', card1)
     player_1_cards.append(card1)
     del deck_of_cards[0]
     print (deck_of_cards)
     print (player_1_cards)  
     player_1game = int (input('Введіть 1, якщо хочете взяти ще карту і 0, в протилежному випадку): '))
    

print('Сума ваших карт:', sum(player_1_cards))


player_2game = int (input('Введіть будь яке число крім 0, якщо хочете взяти ще карту: '))
while (player_2game != 0):
     card2 = deck_of_cards[0]
     print('Ваша карта: ', card2)
     player_2_cards.append(card2)
     del deck_of_cards[0]
     print (deck_of_cards)
     print (player_2_cards)  
     player_2game = int (input('Введіть 1, якщо хочете взяти ще карту і 0, в протилежному випадку): '))
    

print('Сума ваших карт:', sum(player_2_cards))

if (sum(player_1_cards) > 21 and sum(player_2_cards) <= 21):
     print('Гравець 1 програв' )
elif (sum(player_2_cards) > 21 and sum(player_1_cards) <= 21):
     print('Гравець 2 програв')
elif (sum(player_2_cards) > sum(player_1_cards) and sum(player_2_cards) <= 21):
     print('Гравець 2 виграв')
elif (sum(player_1_cards) > sum(player_2_cards) and sum(player_1_cards) <= 21):
     print('Гравець 1 виграв')
else:
     print('LOX')