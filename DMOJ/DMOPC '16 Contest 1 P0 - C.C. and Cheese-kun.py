# https://dmoj.ca/problem/dmopc16c1p0

W = int(input())
C = int(input())

if W == 3 and C >= 95 :
    print("C.C. is absolutely satisfied with her pizza.")
elif W == 1 and C <= 50 :
    print("C.C. is fairly satisfied with her pizza.")
else :
    print("C.C. is very satisfied with her pizza.")