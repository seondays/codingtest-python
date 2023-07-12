# http://usaco.org/index.php?page=viewproblem2&cpid=376

input_file = open("skidesign.in",'r')
ouput_file = open("skidesign.out",'w')

n = int(input_file.readline())

# start~end 사이의 범위로 언덕을 만들기 위해 드는 비용을 계산한다.
def cost_for_range(lst,start,end):
    total_cost = 0

    for i in lst:
        if i < start:
            total_cost += (start-i) ** 2
        elif i > end:
            total_cost += (i-end) ** 2
    
    return total_cost

#main
hills = []

for i in range(n):
    hill = int(input_file.readline())

    hills.append(hill)

min_cost = float('inf')

for i in range(0,101):
    cost = cost_for_range(hills,i,i+17)
    
    if cost < min_cost:
        min_cost = cost

ouput_file.write(str(min_cost))