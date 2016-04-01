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
    'D': 'Diamonds',
    'C': 'Clubs',
    'H': 'Hearts',
    'S': 'Spades',
}

deck = [{'suit': s, 'value': v} for v in value for s in suits]
random.shuffle(deck)
deck1 = deque(deck[:26])
deck2 = deque(deck[26:])

# deck2 = deque([{'suit': s, 'value': v} for v in value for s in suits])
# random.shuffle(deck2)

turn = 1
ante = []

while len(deck1) > 0 and len(deck2) > 0:
    print('TURN {}'.format(turn))
    print("D1: {} \t D2: {}".format(len(deck1), len(deck2)))

    card1 = deck1.popleft()
    card2 = deck2.popleft()
    ante.append(card1)
    ante.append(card2)
    card1['display'] = '{} of {}'.format(card1['value'], suits[card1['suit']])
    card2['display'] = '{} of {}'.format(card2['value'], suits[card2['suit']])
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
        if len(deck1) > 1:
            ante.append(deck1.popleft())
        if len(deck1) > 1:
            ante.append(deck1.popleft())
        if len(deck2) > 1:
            ante.append(deck2.popleft())
        if len(deck2) > 1:
            ante.append(deck2.popleft())

    turn += 1


print('\n\n<><><><><><><><><><><><><><><><><><><>><')
if len(deck1) > len(deck2):
    print("Player One wins the game with {} cards!".format(len(deck1)))
else:
    print("Player Two wins the game with {} cards!".format(len(deck2)))