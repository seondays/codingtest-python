# http://usaco.org/index.php?page=viewproblem2&cpid=893

input_file = open('guess.in','r')
output_file = open('guess.out','w')

characteristic = []
result = 0

for line in input_file:
    line = line.split()
    characteristic.append(line[2: len(line)])

for i in range(len(characteristic)):
    for j in range(i+1,len(characteristic)):
        common = set(characteristic[i]).intersection(set(characteristic[j]))
        result = max(len(common)+1,result)

output_file.write(str(result))

