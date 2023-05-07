# http://usaco.org/index.php?page=viewproblem2&cpid=711

#  소의 정보 읽기
def read_cows(input_file, count):
    cows = [[],[],[],[],[],[],[],[],[],[]]
    for i in range(count):
        cow = list(map(int,input_file.readline().split()))
        cow_number = cow[0]-1
        cow_location = cow[1]
        cows[cow_number].append(cow_location)
    
    return cows
    
# 각 소들의 관찰 데이터 값 얻기

# 관찰 데이터 값으로 소들이 길을 몇번 건넜는지 계산하기

# main

input_file = open('DMOJ\\crossroad.in','r')
ouput_file = open('DMOJ\\crossroad.out','w')

count = int(input_file.readline().strip())
cows = read_cows(input_file,count)


