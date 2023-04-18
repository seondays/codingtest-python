# https://dmoj.ca/problem/crci07p1

# TODO : 플랫폼 위치 저장 후, 층수대로 정렬하기

count = int(input())
before_sort = []
altitude = []
horizontal_coordinates = []

for i in range(count):
    platform = list(map(int,input().split(" ")))
    before_sort.append(platform)

new_platforms = sorted(before_sort,key=lambda x:x[0])

for i in range(count):
    altitude.append(new_platforms[i][0])
    horizontal_coordinates.append(new_platforms[i][1:3])
    

# TODO : 플랫폼 위치가 겹치는지 확인하기

def check_scope(coordinate_list,target):
    if coordinate_list[0] < target and coordinate_list[1] > target:
        return True
    return False

# main

pillars = 0

for i in range(count):
    if i == 0:
        pillars += altitude[i] * 2
    if i != 0:
        for j in range(i-1,-1,-1):
            if check_scope(horizontal_coordinates[j],horizontal_coordinates[i][0]) or horizontal_coordinates[j][0] == horizontal_coordinates[i][0]:
                pillars += altitude[i]- altitude[j]
                break
            else:
                if j == 0:
                    pillars += altitude[i]
        
        for j in range(i-1,-1,-1):   
            if check_scope(horizontal_coordinates[j],horizontal_coordinates[i][1]) or horizontal_coordinates[j][1] == horizontal_coordinates[i][1]:
                pillars += altitude[i]- altitude[j]
                break
            else:
                if j == 0:
                    pillars += altitude[i]

print(pillars)