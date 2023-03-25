# https://dmoj.ca/problem/wac3p3

moves = input()
num_combos = int(input())

combos = {}
for i in range(num_combos):
    combo, points = input().strip().split()
    combos[combo] = int(points)

score = 0
current_move = 0

while current_move < len(moves):
    found_combo = False
    for i in range(len(moves) - current_move, 0, -1):
        combo = moves[current_move:current_move+i]
        if combo in combos:
            score += combos[combo]
            current_move += i
            found_combo = True
            break
    
    if not found_combo:
        current_move += 1

print(score+len(moves))







