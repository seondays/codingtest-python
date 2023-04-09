# https://dmoj.ca/problem/ccc99s1

def chack_no_high_in_list(list):
    if 'jack' in list or 'queen' in list or 'king' in list or 'ace' in list:
        return False
    return True

CARDS_NUM = 52
deck = []

for i in range(CARDS_NUM):
    input_card = input()
    deck.append(input_card)

A_point = 0
B_point = 0
remaining = CARDS_NUM

for i in range(CARDS_NUM):
    point = 0
    card = deck[i]
    remaining -= 1
    player = ''
    
    if card == 'jack' and remaining >= 1 and chack_no_high_in_list(deck[i+1]):
        point += 1
    if card == 'queen' and remaining >= 2 and chack_no_high_in_list(deck[i+1:i+3]):
        point += 2
    if card == 'king' and remaining >= 3 and chack_no_high_in_list(deck[i+1:i+4]):
        point += 3
    if card == 'ace' and remaining >= 4 and chack_no_high_in_list(deck[i+1:i+5]):
        point += 4
        
    if i % 2 == 0:
        A_point += point
        player = 'A'
    if i % 2 != 0:
        B_point += point
        player = 'B'
    
    if point > 0:
        print(f"Player {player} scores {point} point(s).")
    
print(f"Player A: {A_point} point(s).")
print(f"Player B: {B_point} point(s).")
