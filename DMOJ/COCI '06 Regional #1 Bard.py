# https://dmoj.ca/problem/crci06p1

people = int(input())
nights = int(input())

# 주민들의 출현 횟수를 담을 딕셔너리 만들기
def make_dict(people):
    dict = {}

    for i in range(1,people+1):
        dict[i] = []

    return dict

# main
people_dict = make_dict(people)

for i in range(nights):
    tonight = list(map(int,input().split()))[1:]

    # 바드가 새로운 노래를 알려주는 경우(i번째 노래라고 지칭)
    if 1 in tonight:
        for k in range(len(tonight)):
            people_dict[tonight[k]].append(i)
    
    # 주민들끼리 노래를 공유하는 경우(주민들이 아는 노래들을 모두 합친 노래의 목록을 구한다)
    elif 1 not in tonight:
        lst = []

        for k in range(len(tonight)):
            lst.extend([i for i in people_dict[tonight[k]]])
        
        for k in range(len(tonight)):
            people_dict[tonight[k]] = list(set(lst))

# 모든 노래의 개수
song = max([len(k) for k in people_dict.values()])

# 해당 노래를 모두 알고있는 주민 출력
for k in people_dict.keys():
    if len(people_dict[k]) == song:
        print(k)
