# https://dmoj.ca/problem/wac3p3

# 입력 처리
moves = input()
combo_count = int(input())
combos = dict()

for i in range(combo_count):
    combo = input().split()
    combos[combo[0]] = int(combo[1])

# 전체 움직임에서 콤보를 찾아내기
score = 0 
i = 0

while i < len(moves):
    canadidate_list = []
    
    for k in range(i+1,len(moves)):
        tmp = moves[i:k]
        if tmp in combos:
            canadidate_list.append(tmp)

    # 찾아낸 콤보들 중 가장 길이가 긴 콤보를 선택하기
    if len(canadidate_list) > 0 :
        combo = max(canadidate_list, key= len)
        score += combos[combo]
        i += len(combo)
    else:
        i += 1
    
# 기본 점수를 더해주기
score += len(moves)

print(score)
    








