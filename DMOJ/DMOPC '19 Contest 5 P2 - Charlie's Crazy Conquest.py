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

# 게임 로직 구현
index = 1
while (player_hp > 0 and enemy_hp > 0) and index < (turn * 2) + 1:
    # 만약 공격이면
    if act[index] == 'A':
        # 이전에 회피하지 않았으면 그대로 공격이 들어간다
        if act[index - 1] != 'D':
            if index % 2 == 0:
                player_hp -= val[index]
            else :
                enemy_hp -= val[index]
    # 만약 회피라면
    if act[index] == 'D':
        # 다음에 공격이 아니라면 내가 스스로 데미지를 입는다
        if act[index + 1] != 'A':
            if index % 2 == 0:
                enemy_hp -= val[index]
            else:
                player_hp -= val[index]
    index += 1

# 결과 출력
if player_hp > 0 and enemy_hp < 1:
    print("VICTORY")
elif enemy_hp > 0 and player_hp < 1:
    print("DEFEAT")
elif player_hp > 0 and enemy_hp > 0:
    print("TIE")