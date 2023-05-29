# http://usaco.org/index.php?page=viewproblem2&cpid=736

input_file = open('cownomics.in','r')
output_file = open('cownomics.out','w')

spotty = []
plain = []

# 점박이 소와 일반 소 정보 읽어오기
n_lst = input_file.readline().strip().split(' ')
n = int(n_lst[0])
m = int(n_lst[1])

def read_cows(input_file,n):
    cow_lst = []

    for i in range(n):
        genome = input_file.readline().strip()
        cow_lst.append(genome)
    
    return cow_lst

# 유전자 갯수만큼의 리스트 만들기
def positions_lst():
    lst = ['']*m

    return lst

# 유전자를 순서 리스트에 차례대로 저장하기
def save_position(genome,position_lst):
    for i in range(m):
        position_lst[i] = position_lst[i] + genome[i]

    return position_lst

# 점박이 소와 일반 소의 유전자 풀이 겹치는지 확인하기
def check_set(spotty,plain):
    count = 0

    for i in range(m):
        if len(set(spotty[i]) & set(plain[i])) == 0:
            count += 1
    
    return count

# main
spotty = read_cows(input_file,n)
spotty_position_lst = positions_lst()

for i in spotty:
    spotty_position_lst = save_position(i,spotty_position_lst)

plain = read_cows(input_file,n)
plain_position_lst = positions_lst()

for i in plain:
    plain_position_lst = save_position(i,plain_position_lst)

output_file.write(str(check_set(spotty_position_lst,plain_position_lst)))




