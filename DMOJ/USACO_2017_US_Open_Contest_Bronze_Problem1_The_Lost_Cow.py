# http://usaco.org/index.php?page=viewproblem2&cpid=735

# 전진 위치 계산하기
def calculate_location(x,count,zigzag):
    if count % 2 == 0:
        x -= zigzag
    if count % 2 != 0:
        x += zigzag
    
    return x

# 이동거리 구하기
def moving(location,zigzag_location,y):
    move = 0
    if zigzag_location > y:
        move = abs(y - location)
        return move
    if zigzag_location <= y:
        move = abs(zigzag_location-location)
        return move
    
# main
input_file = open('DMOJ/lostcow.in','r')
output_file = open('DMOJ/lostcow.out','w')

location_info = list(map(int,input_file.readline().split()))
x = location_info[0]
y = location_info[1]
location = x
zigzag = 1
count = 1
total_move = 0

while location < y:
    zigzag_location = calculate_location(x,count,zigzag)
    total_move += moving(location,zigzag_location,y)
    location = zigzag_location
    count += 1
    zigzag *= 2

output_file.write(str(total_move))
