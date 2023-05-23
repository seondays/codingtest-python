# https://dmoj.ca/problem/ccc18j3

distance = list(map(int,input().split()))

towns = [0]

for i in range(len(distance)):
    town = distance[i] + towns[i]
    towns.append(town)

for i in range(len(towns)):
    d = []
    for j in range(len(towns)):
        between = towns[i] - towns[j]
        d.append(between)
    print(*list(map(lambda x : abs(x),d)))