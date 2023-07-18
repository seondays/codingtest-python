# http://usaco.org/index.php?page=viewproblem2&cpid=1323

input_n = int(input())
input_text = input()

replace_to_b = input_text.replace('F','B')
replace_to_e = input_text.replace('F','E')

answer = []
result = 0
for i in range(len(input_text)):
    if i == len(input_text)-1:
        break

    exci = replace_to_b[i:i+2]

    if exci[0] == exci[1]:
        result += 1

answer.append(result)
result = 0

for i in range(len(input_text)):
    if i == len(input_text)-1:
        break

    exci = replace_to_e[i:i+2]

    if exci[0] == exci[1]:
        result += 1

answer.append(result)

print(len(answer))
print(*answer,sep="\n")
