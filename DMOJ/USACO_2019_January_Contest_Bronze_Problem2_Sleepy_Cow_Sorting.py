# http://usaco.org/index.php?page=viewproblem2&cpid=892

input_file = open('sleepy.in','r')
output_file = open('sleepy.out','w')

n = int(input_file.readline().strip())
cows = [int(i) for i in input_file.read().strip().split()]

def find_sorted_length(cows):
    length = 1
    for i in range(len(cows)-1,-1,-1):
        if cows[i] > cows[i-1]:
            length += 1
        else:
            break
    return length

output_file.write(str(n-find_sorted_length(cows)))