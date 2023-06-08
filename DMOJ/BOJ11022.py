# https://www.acmicpc.net/problem/11022

n = int(input())

for i in range(1,n+1):
    input_number = input().split()

    a = int(input_number[0])
    b = int(input_number[1])

    print(f"Case #{i}: {a} + {b} = {a+b}")