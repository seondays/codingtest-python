# https://dmoj.ca/problem/dmopc19c5p1

input_n = list(map(int,input().split()))
item_n = input_n[0]
assignment_n = input_n[1]

# 준비물 저장하기
items = []

for i in range(item_n):
    item = input()
    items.append(item)

# 과제 확인하기
complete = 0

for i in range(assignment_n):
    is_in = True
    n = int(input())

    for k in range(n):
        need = input()

        if need not in items:
            is_in = False
            continue

        if k == n-1 and is_in:
            complete += 1

print(complete)