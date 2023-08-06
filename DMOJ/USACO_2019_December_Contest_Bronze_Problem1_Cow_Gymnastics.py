# http://usaco.org/index.php?page=viewproblem2&cpid=963

input_file = open('gymnastics.in','r')
output_file = open('gymnastics.out','w')

n = input_file.readline().split()
sessions = int(n[0])
performance = int(n[1])
dict = {}
result = 0

for i in range(sessions):
    session = list(map(int,input_file.readline().split()))
    for j in range(performance):
        for k in range(j+1,performance):
                tmp = (session[j],session[k])
                if tmp in dict:
                      dict[tmp] += 1
                else:
                      dict[tmp] = 1

input_file.close()
output_file.close()