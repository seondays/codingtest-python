# http://usaco.org/index.php?page=viewproblem2&cpid=359

import bisect

input_file = open('baseball.in','r')
output_file = open('baseball.out','w')

n = int(input_file.readline())

positions = []
total = 0

for i in range(n):
    positions.append(int(input_file.readline()))

positions.sort()

for i in range(n):
    for j in range(i+1,n):
        difference = positions[j]-positions[i]
        left = bisect.bisect_left(positions,positions[j] + difference)
        right = bisect.bisect_right(positions,positions[j] + difference * 2)
        total += right - left
        
output_file.write(str(total))