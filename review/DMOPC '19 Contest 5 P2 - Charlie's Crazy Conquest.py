# https://dmoj.ca/problem/dmopc19c5p2

input_text = input().split(" ")

turn = int(input_text[0])
player_health = int(input_text[1])
enemy_health = int(input_text[1])

player_move = []
player_damage = []
enemy_move = []
enemy_damage = []

for i in range(1,turn*2+1):
    move = input().split(" ")
    if i <= turn:
        player_move.append(move[0])
        player_damage.append(int(move[1]))
    
    if i > turn:
        enemy_move.append(move[0])
        enemy_damage.append(int(move[1]))

move = []
damage = []

for i in range(turn):
    move.append(player_move[i])
    move.append(enemy_move[i])
    damage.append(player_damage[i])
    damage.append(enemy_damage[i])


for i in range(len(move)):
    
    if i % 2 == 0:
        if i == 0 and move[i] == 'A':
            enemy_health -= damage[i]
        if i != 0 and move[i] == 'A':
            if move[i-1] == 'A':
                enemy_health -= damage[i]
        if move[i] == 'D':
            if move[i+1] == 'D':
                player_health -= damage[i]
    
    if i % 2 != 0:
        if move[i] == 'A':
            if move[i-1] == 'A':
                player_health -= damage[i]
        if move[i] == 'D' and i == len(move)-1:
            enemy_health -= damage[i]
        if move[i] == 'D' and i != len(move)-1:
            if move[i+1] == 'D':
                enemy_health -= damage[i]
       
    if player_health <= 0 :
        print("DEFEAT")
        break
    if enemy_health <= 0 :
        print("VICTORY")
        break

if player_health > 0 and enemy_health > 0 :
    print("TIE")   
        
    
    
    
    
    

