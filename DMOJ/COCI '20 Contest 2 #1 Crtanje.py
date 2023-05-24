# https://dmoj.ca/problem/coci20c2p1

n = int(input())
row = list(input())

draw = []
count = 0

for i in range(n):
    if row[i] == '+':
        draw.append(count)
        count += 1
    if row[i] == '-':
        count -= 1
        draw.append(count)
    if row[i] == '=':
        draw.append(count)

min_value = min(draw)
if min_value < 0:
    draw = list(map(lambda x : x+abs(min_value),draw))

graph = [['.' for j in range(n)]for i in range(max(draw)+1)]

for i in range(n):
    if row[i] == '+':
        graph[draw[i]][i] = '/'
    if row[i] == '-':
        graph[draw[i]][i] = '\\'
    if row[i] == '=':
        graph[draw[i]][i] = '_'

for i in range(len(graph)-1,-1,-1):
    print(''.join(graph[i]))

