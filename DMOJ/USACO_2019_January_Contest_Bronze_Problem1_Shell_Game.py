# http://usaco.org/index.php?page=viewproblem2&cpid=891

input_file = open('shell.in','r')
output_file = open('shell.out','w')

n = int(input_file.readline().strip())
round = [[int(j) for j in i.split()] for i in input_file.read().strip().split('\n')]
