# http://usaco.org/index.php?page=viewproblem2&cpid=965

# input_file = open('DMOJ/lineup.in','r')
# output_file = open('DMOJ/lineup.out','w')
# cows = ["Beatrice","Belinda","Bella","Bessie","Betsy","Blue","Buttercup","Sue"]

# # 정보 읽어오기
# count = int(input_file.readline().strip())

# # 주어진 인접 조건에 알맞게 소 리스트를 반환
# def return_cow_constrain(sentence):
#     list_cow = []
#     list_cow.append(sentence.split()[0])
#     list_cow.append(sentence.split()[-1])

#     return sorted(list_cow)

# # 전체 소 조건 리스트 만들기
# constrain_list = []
# for i in range(count):
#     constrain_list.append(return_cow_constrain(input_file.readline()))

# # 해당 소의 짝꿍 소 리스트 반환
# def return_pairs_list(constrain_list,cow):
#     pairs = []
#     for i in constrain_list:
#         if cow in i:
#             for j in i:
#                 if cow != j:
#                     pairs.append(j)
#     return pairs

# #main
# result = []
# for i in cows:
#     pair = return_pairs_list(constrain_list,i)
#     if len(pair) == 0:
#         result.append(i)

from functools import lru_cache

with open("DMOJ/lineup.in") as fin:
    data = fin.read().split("\n")
    
cows = [
    "Bessie",
    "Buttercup",
    "Belinda",
    "Beatrice",
    "Bella",
    "Blue",
    "Betsy",
    "Sue"
]
cows.sort()

# Parse the input into a list of pairs
n = int(data[0])
constraints = []
for i in range(1, n + 1):
    words = data[i].split(" ")
    pair = [cows.index(words[0]), cows.index(words[-1])]
    
    constraints.append(pair)
    
    
def permutations(nums):
    # Generate all permutations of nums
    n = len(nums)
    if n == 1:
        return [nums]
        
    results = []
    for start in range(n):
        for p in permutations(nums[:start] + nums[start + 1:]):
            perm = [nums[start]] + p
            results.append(perm)
            
    return results


for p in permutations(list(range(8))):
    works = True
    for cow1, cow2 in constraints:
        if abs(p.index(cow1) - p.index(cow2)) != 1:
            works = False
            break
            
    if works:
        # Convert list of integers to list of cow names
        ans = [cows[i] for i in p]
        break
        
with open("DMOJ/lineup.out", "w") as fout:
    fout.write("\n".join(ans) + "\n")

