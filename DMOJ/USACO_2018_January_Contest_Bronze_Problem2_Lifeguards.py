# http://usaco.org/index.php?page=viewproblem2&cpid=784

input_file = open('lifeguards.in','r')
ouput_file = open('lifeguards.out','w')

#fired에 있는 직원을 해고했을 때 근무할 수 있는 총 시간 구하기
def num_covered(time_lst,fired):
    result = set()

    for i in range(len(time_lst)):
        if i != fired:
            for j in range(time_lst[i][0],time_lst[i][1]):
                result.add(j)
    
    return (len(result))

# main
n = int(input_file.readline())
lifeguards = []

for i in range(n):
    guard = list(map(int,input_file.readline().split()))
    lifeguards.append(guard)

max_value = 0

for i in range(n):
    result = num_covered(lifeguards,i)
    if max_value < result:
        max_value = result

ouput_file.write(str(max_value))
