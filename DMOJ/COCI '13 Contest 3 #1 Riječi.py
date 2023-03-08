# https://dmoj.ca/problem/coci13c3p1

push_count = int(input())

a = 1
b = 0

for i in range(0,push_count):
    a_change = b
    b_change = a+b

    a = a_change
    b = b_change

print(a,b)
