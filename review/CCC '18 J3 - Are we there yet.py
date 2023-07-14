# https://dmoj.ca/problem/ccc18j3

input_text = list(map(int,"3 10 12 5".split()))

first_town = [0]

for i in range(1,5):
    first_town.append(first_town[i-1] + input_text[i-1])

print(*first_town)

for i in range(1,5):
    # 1234
    town = []

    for k in range(4):
        #0123
        if i-1 <= k:
            town.append(abs(input_text[k])-first_town[i-1])
        else:
            town.append(input_text[k]+first_town[i-1])

    print(*town)
    first_town = town