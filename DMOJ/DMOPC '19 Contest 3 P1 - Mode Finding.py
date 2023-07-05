# https://dmoj.ca/problem/dmopc19c3p1

n = int(input())
lst = input().split()
d = {}

for i in range(n):
    if lst[i] not in d:
        d[lst[i]] = 1
    else:
        d[lst[i]] += 1

max_value = max(d.values())
result_lst = sorted([int(k) for k,v in d.items() if v == max_value])

print(*result_lst)