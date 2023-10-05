# https://dmoj.ca/problem/dmopc19c5p2

info = list(map(int,input().split()))
turn = info[0]

# 플레이어와 적의 체력 설정
player_hp = info[1]
enemy_hp = info[1]

# 플레이어의 행동 리스트 설정
player_act = []
player_val = []

for i in range(turn):
    info = input().split()
    player_act.append(info[0])
    player_val.append(int(info[1]))

# 적의 행동 리스트 설정
enemy_act = []
enemy_val = []

for i in range(turn):
    info = input().split()
    enemy_act.append(info[0])
    enemy_val.append(int(info[1]))

# 최종 행동 리스트 생성
act = ['dummy']
val = [-1]
for i in range(turn):
    act.append(player_act[i])
    act.append(enemy_act[i])
    val.append(player_val[i])
    val.append(enemy_val[i])
act.append('dummy')
val.append(-1)