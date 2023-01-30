# https://dmoj.ca/problem/ccc18j2

parking_space = int(input())
yesterday_space = input()
today_space = input()
count = 0

for i in range(parking_space) :
    if today_space[i] == "C" and yesterday_space[i] == "C" :
        count += 1
        
print(count)