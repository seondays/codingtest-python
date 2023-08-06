# http://usaco.org/index.php?page=viewproblem2&cpid=963

input_file = open('DMOJ/gymnastics.in','r')
output_file = open('DMOJ/gymnastics.out','w')

n = input_file.readline().split()
sessions = int(n[0])
performance = int(n[1])
dict = {}

for i in range(sessions):
    session = list(map(int,input_file.readline().split()))
    for j in range(performance):
        for k in range(j+1,performance):
            
                tmp = []
                tmp.append(session[j])
                tmp.append(session[k])
                tmp = tuple(tmp)

                if tmp in dict:
                      dict[tmp] += 1
                else:
                      dict[tmp] = 1

print(dict)



input_file.close()
output_file.close()