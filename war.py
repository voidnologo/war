import random
from collections import deque


value = {
    'Ace': 14,
    'King': 13,
    'Queen': 12,
    'Jack': 11,
    '10': 10,
    '9': 9,
    '8': 8,
    '7': 7,
    '6': 6,
    '5': 5,
    '4': 4,
    '3': 3,
    '2': 2,
}

suits = {
    'D': '\u2662',
    'C': '\u2667',
    'H': '\u2661',
    'S': '\u2664',
}

def ante_up(ante, deck, number): 
    for _ in range(number): 
        if len(deck) > 1:
            ante.append(deck.popleft())
        else:
            break

def draw_to_ante(ante, deck):
    card = deck.popleft()
    ante.append(card)
    return card


deck = [{'suit': s, 'value': v, 'display': '{}{}'.format(v, suits[s])} for v in value for s in suits]
random.shuffle(deck)
deck1 = deque(deck[:26])
deck2 = deque(deck[26:])

turn = 1
ante = []

while len(deck1) > 0 and len(deck2) > 0:
    print('TURN {}'.format(turn))
    if turn % 2000 == 0:
        random.shuffle(deck1)
        random.shuffle(deck2)
    print("D1: {} \t D2: {}".format(len(deck1), len(deck2)))

    card1 = draw_to_ante(ante, deck1)
    card2 = draw_to_ante(ante, deck2)
    print("Player One has: {}".format(card1['display']))
    print("Player Two has: {}".format(card2['display']))
    if value[card1['value']] > value[card2['value']]:
        print("Player One wins.")
        deck1.extend(ante)
        ante = []
    elif value[card2['value']] > value[card1['value']]:
        print("Player Two wins.")
        deck2.extend(ante)
        ante = []
    else:
        print("Tie!")
        ante_up(ante, deck1, 2)
        ante_up(ante, deck2, 2)

    turn += 1


print('\n\n<><><><><><><><><><><><><><><><><><><>><')
if len(deck1) > len(deck2):
    print("Player One wins!")
else:
    print("Player Two wins!")