# https://www.acmicpc.net/problem/2562
lst = []

for i in range(9):
    n = int(input())
    lst.append(n)

print(max(lst))
print(lst.index(max(lst))+1)