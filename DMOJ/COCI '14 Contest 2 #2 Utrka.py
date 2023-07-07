# https://dmoj.ca/problem/coci14c2p2

n = int(input())
contestant = {}
complete = {}

# 참가자 저장
for i in range(n):
    marathoner = input()
    
    if marathoner in contestant:
        contestant[marathoner] += 1
    else:
        contestant[marathoner] = 1

# 완주자 저장
for i in range(n-1):
    marathoner = input()
    
    if marathoner in complete:
        complete[marathoner] += 1
    else:
        complete[marathoner] = 1

# 완주하지 못한 사람 구하기
for k in complete.keys():
    contestant[k] = contestant[k] - complete[k]

print(*[k for k in contestant.keys() if contestant[k] == 1])