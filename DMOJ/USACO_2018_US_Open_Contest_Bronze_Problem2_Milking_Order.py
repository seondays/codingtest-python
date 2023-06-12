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

# 우선순위를 가진 소들을 하나씩 배치하는 리스트를 만들기      
def set_hierarchy_order(hierarchy_order,cows_order):
    for i in range(len(hierarchy_order)):
        for j in range(len(cows_order)):
            if hierarchy_order[i] not in cows_order:
                if cows_order[j] == 0:
                    cows_order[j] = hierarchy_order[i]
        continue
        
    return cows_order

# 소의 순서가 올바른지 체크
def check_hierarchy(cows_order,hierarchy_order):
    for i in range(len(hierarchy_order)-1):
        for j in range(len(hierarchy_order)-1,i,-1):
            if cows_order.index(hierarchy_order[i]) > cows_order.index(hierarchy_order[j]):
                return False
    return True

#main
num_fix_order = num_cows[2]
cows_order = [0] * num_cows[0]
first_cow_order = 0

# 고정자리가 있는 소들 세팅하기
for i in range(num_fix_order):
    fix_lst = list(map(int,input_file.readline().split()))
    cows_order = fixed_cow(cows_order,fix_lst)

for i in range(num_cows[0]):
    if cows_order[i] == 0:
        tem_lst = set_number_one_cow(cows_order,i)
        tem_lst = set_hierarchy_order(hierarchy_order,tem_lst)
        if check_hierarchy(tem_lst,hierarchy_order):
            first_cow_order = tem_lst.index(1)
            break

ouput_file.write(str(first_cow_order+1))