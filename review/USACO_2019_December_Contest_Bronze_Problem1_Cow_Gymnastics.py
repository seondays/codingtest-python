# http://usaco.org/index.php?page=viewproblem2&cpid=963

input_file = open('gymnastics.in','r')
output_file = open('gymnastics.out','w')

number_of_sessions, number_of_cows = [int(i) for i in input_file.readline().split()]
sessions = []
for i in range(number_of_sessions):
        sessions.append(list(int(i)-1for i in input_file.readline().split()))

check = [[0 for k in range(number_of_cows)] for i in range(number_of_cows)]
for i in range(number_of_sessions):
    for j in range(number_of_cows):# cow1
            for k in range(j+1,number_of_cows):# cow2
                   index1=sessions[i][j]
                   index2=sessions[i][k]
                   check[sessions[i][j]][sessions[i][k]] += 1

count = 0
for i in check:
       count += i.count(number_of_sessions)

output_file.write(str(count))

input_file.close()
output_file.close()