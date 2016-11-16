import random

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
random.shuffle(cards)
print(cards)#TODO delete

#Round 1
computer_cards = cards.pop()
my_cards = cards.pop()
print('Your card: ' + str(my_cards))
print('Computer card: ' + str(computer_cards))
do_hit = raw_input('\nIf you want to stay type \'s\', if you want to hit type \'h\': ')
if do_hit == 'h':
    my_cards.add(cards.pop())
computer_cards.add(cards.pop())
#Round 2
print('Your cards: ' + str(my_cards))
print('Computer cards: ' + str(computer_cards))
do_hit = raw_input('\nIf you want to stay type \'s\', if you want to hit type \'h\': ')
if do_hit == 'h':
    my_cards.add(cards.pop())
if computer_cards[0] + computer_cards[1] < 16:
    computer_cards.add(cards.pop())
print('Your cards: ' + str(my_cards))
print('Computer cards: ' + str(computer_cards))
