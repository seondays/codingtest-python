# http://usaco.org/index.php?page=viewproblem2&cpid=893

input_file = open('guess.in','r')
output_file = open('guess.out','w')

n = int(input_file.readline())
animals = {}

for i in range(n):
    line = input_file.readline().split()
    animals[line[0]] = set(line[2:])
    
max_size = 0
for key1 in animals:
    for key2 in animals:
        if key1 != key2 :
            size = len(animals[key1] & animals[key2])
            if size > max_size:
                max_size = size

output_file.write(str(max_size+1))


