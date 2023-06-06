# http://usaco.org/index.php?page=viewproblem2&cpid=915

input_file = open('herding.in','r')
output_file = open('herding.out','w')

locations = list(map(int,input_file.read().strip().split()))

# 세 소의 위치가 일렬로 이웃해 있는지 확인하기
def is_consecutive(lst):
    if lst[0]-lst[1] == -1 and lst[1]-lst[2] == -1:
        return True
    return False

# 위치의 차를 계산해서 리스트로 반환하기
def calculate_difference(lst):
    return_lst = []

    return_lst.append(abs(lst[0]-lst[1]))
    return_lst.append(abs(lst[1]-lst[2]))

    return return_lst

# 한번만에 옮길 수 있는지 체크해서 min 횟수 구하기
def counter_move_once(lst):
    if 2 in lst:
        return 1
    return 2

# max 횟수 구하기
def counter_max(lst):
    return max(lst)-1

#main
count_min = 0
count_max = 0

if is_consecutive(locations):
    output_file.write(str(count_min) + "\n")
    output_file.write(str(count_max))
else:
    difference = calculate_difference(locations)
    count_min = counter_move_once(difference)
    count_max = counter_max(difference)

    output_file.write(str(count_min) + "\n")
    output_file.write(str(count_max))