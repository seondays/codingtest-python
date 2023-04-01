# https://dmoj.ca/problem/coci19c5p1

input_size = input().split(" ")

high = int(input_size[0])
wide = int(input_size[1])

pictures = []
count = 0

for i in range(high):
    row = input()
    pictures.append(row)

for i in range(high):
    for j in range(wide):
        if pictures[i][j] == '*':
            if i == 0 and j == 0 :
                count += 1
            elif i == 0 and pictures[i][j-1] == '.':
                count += 1
            elif j == 0 and pictures[i-1][j] == '.':
                count += 1
            elif pictures[i-1][j] == '.' and pictures[i][j-1] == '.':
                count += 1

print(count)