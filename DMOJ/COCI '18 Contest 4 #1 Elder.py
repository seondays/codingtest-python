# https://dmoj.ca/problem/coci18c4p1

wizard = input()
fight_count = int(input())
answer = [wizard]

for i in range(0,fight_count) :
    fight = input().split(" ")
    
    if fight[1] == wizard :
        wizard = fight[0]
        answer.append(wizard)

answer = set(answer)

print(wizard)
print(len(answer))