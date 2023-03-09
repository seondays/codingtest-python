# https://dmoj.ca/problem/ccc18s1

villages_count = int(input())
villages = []

for i in range(0,villages_count):
    village = int(input())
    villages.append(village)

villages.sort()
villages_size = []

for i in range(1, len(villages)-1):
    size = (villages[i] - villages[i-1]) /2 + (villages[i+1] - villages[i]) /2
    villages_size.append(size)

print(min(villages_size))
