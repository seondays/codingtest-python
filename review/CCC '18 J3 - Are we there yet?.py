# https://dmoj.ca/problem/ccc18j3

# TODO : 입력받아서, 리스트로 저장
distance = list(map(int,input().split(" ")))

# TODO : 마을 주소를 구한다.

cities = [0]

for i in range(4):
    cities.append(cities[i]+distance[i])

# TODO : i번째 마을과 얼마나 떨어져있는지 계산하여 출력하기

for i in range(5):
    a = []
    for j in range(5):
        d = cities[i] - cities[j]
        if d < 0:
            d *=  -1
        a.append(d)
    
    print(*a)