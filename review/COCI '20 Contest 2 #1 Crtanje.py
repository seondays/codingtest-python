# https://dmoj.ca/problem/coci20c2p1

input_len = int(input())
input_sentence = input()

pictures = []
coordinate = []
standard = 0

for i in input_sentence:
    if i == '+':
        coordinate.append(standard)
        standard += 1
    if i == '-':
        standard -= 1
        coordinate.append(standard)
    if i == '=':
        coordinate.append(standard)

min_value = min(coordinate)

coordinate = list(map(lambda x:x-min_value,coordinate))
row_count = max(coordinate)+1

for i in range(row_count):
    row = ['.' for j in range(input_len)]
    pictures.append(row)

for i in range(input_len):
    if input_sentence[i] == '+':
        pictures[coordinate[i]][i] = '/'
    if input_sentence[i] == '-':
        pictures[coordinate[i]][i] = '\\'
    if input_sentence[i] == '=':
        pictures[coordinate[i]][i] = '_'

for i in range(len(pictures)-1,-1,-1):
    print(''.join(pictures[i]))
        
    
    




        
