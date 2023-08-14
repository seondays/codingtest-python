# http://usaco.org/index.php?page=viewproblem2&cpid=359

import bisect

input_file = open('baseball.in','r')
output_file = open('baseball.out','w')

n = int(input_file.readline())

positions = []
total = 0

for i in range(n):
    positions.append(int(input_file.readline()))