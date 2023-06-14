input_file = open('DMOJ/milkorder.in','r')
ouput_file = open('DMOJ/milkorder.out','w')

num_cows = list(map(int,input_file.readline().split()))
hierarchy_order = list(map(int,input_file.readline().split()))

# 위치가 정해져 있는 소들 배치하기
def fixed_cow(cows_order,fix_lst):
    num_cow = fix_lst[0]
    order_cow = fix_lst[1] - 1

    cows_order[order_cow] = num_cow

    return cows_order

# 1번 소를 비어 있는 자리 중 가장 앞자리에 배치함
def set_number_one_cow(cows_order,i):
    result = [i for i in cows_order]
    result[i] = 1

    return result


# 현재 주어진 hierarchy 정보의 위치(i+1) 인덱스를 구하는 기능
def get_hierarchy_index(next_i,cows_order):
    if next_i in cows_order:
        return cows_order.index(next_i)
    else:
        return -1

# 위치 인덱스가 i > i+1 이라면 해당 배치는 실패이다
def check_hierarchy(i,next_i):
    if i < next_i:
        return True
    return False

def set_hierarchy_order(cows_order,first_point,second_point,value):
    if second_point not in cows_order:
        cows_order[first_point] = value
    else:
        for i in range(second_point,-1,-1):
            if cows_order[i] == 0:
                cows_order[i] = value
    
    return cows_order
    
def set_last_hierarchy(cows_order,value):
    print(cows_order)
    for i in range(len(cows_order)-1,-1,-1):
        if cows_order[i] == 0:
            cows_order[i] = value
            return cows_order
       
#main
num_fix_order = num_cows[2]
cows_order = [0] * num_cows[0]
first_cow_order = 0
swich = False

# 고정자리가 있는 소들 세팅하기
for i in range(num_fix_order):
    fix_lst = list(map(int,input_file.readline().split()))
    cows_order = fixed_cow(cows_order,fix_lst)
    save_cows_order = [i for i in cows_order]

# 첫번째 빈 자리부터 1을 배치하는 작업
for i in range(num_cows[0]):
    if swich:
        first_cow_order = cows_order.index(1)
        break
    cows_order = save_cows_order
    if cows_order[i] == 0:
        cows_order = set_number_one_cow(cows_order,i)
        # 다시 주어진 리스트를 순회해야 함. [3,0,5,1,0,0] / [4,5,6]
        for j in range(len(hierarchy_order)):
            print("j: ",j)
            if hierarchy_order[j] in cows_order:
                continue

            if j == len(hierarchy_order)-1:
                    cows_order = set_last_hierarchy(cows_order,hierarchy_order[j])
                    swich = True
                    break

            first_point = cows_order.index(0)
            second_point = get_hierarchy_index(hierarchy_order[j+1],cows_order)

            if check_hierarchy(first_point,second_point):
                cows_order = set_hierarchy_order(cows_order,first_point,second_point,hierarchy_order[j])

            else:
                break



ouput_file.write(str(first_cow_order+1))