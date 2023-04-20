# https://dmoj.ca/problem/coci19c5p1

input_text = input().split(" ")

col_len = int(input_text[0])
row_len = int(input_text[1])

matrix = []

for i in range(col_len):
    col = list(input())
    matrix.append(col)

count = 0

for i in range(col_len):
    for j in range(row_len):       
        if matrix[i][j] == '*':
            if j == row_len-1 and i == col_len-1 :
                count += 1
            elif j == row_len-1:
                if matrix[i+1][j] == '.':
                    count += 1
            elif i == col_len-1:
                if matrix[i][j+1] == '.':
                    count += 1
            elif matrix[i+1][j] == '.' and matrix[i][j+1] == '.':
                count += 1

print(count)