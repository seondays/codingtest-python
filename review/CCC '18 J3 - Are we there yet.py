# https://dmoj.ca/problem/ccc18j3

input_text = list(map(int,input().split()))

first_town = [0]

for i in range(1,5):
    first_town.append(first_town[i-1] + input_text[i-1])

for i in range(5):
    town = []

    for k in range(5):
        town.append(abs(first_town[i] - first_town[k]))
    
    print(*town)