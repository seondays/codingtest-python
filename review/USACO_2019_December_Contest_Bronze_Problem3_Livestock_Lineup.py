# http://usaco.org/index.php?page=viewproblem2&cpid=965
from itertools import permutations

input_file = open('lineup.in','r')
output_file = open('lineup.out','w')
cows = ["Beatrice","Belinda","Bella","Bessie","Betsy","Blue","Buttercup","Sue"]
index = [0,1,2,3,4,5,6,7]

# 정보 읽어오기
count = int(input_file.readline().strip())

# 주어진 인접 조건에 알맞게 소 리스트를 반환
def return_cow_constrain(sentence):
    list_cow = []
    list_cow.append(sentence.split()[0])
    list_cow.append(sentence.split()[-1])

    return sorted(list_cow)

# 짝궁 소 인덱스 반환
def return_cow_pairs(list_cow):
    pairs = []
    for i in list_cow:
        pairs.append(cows.index(i))

    return pairs

#main
pairs = []
for i in range(count):
    pairs.append(return_cow_pairs(return_cow_constrain(input_file.readline())))

for i in permutations(index):
    check = True
    for j in pairs:
        if abs(i.index(j[0])-i.index(j[1])) != 1:
            break
    else:
        check = False
    if check == False:
        results = list(i)
        break

for i in results:
    output_file.write(cows[i]+'\n')
