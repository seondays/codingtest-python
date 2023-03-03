# https://dmoj.ca/problem/ecoo13r1p1

count = int(input())

take = 0
serve = 0 

while True:
    s = input()
    if s == "EOF":
        break

    if s == "CLOSE":
        print(take,take-serve,count)
        take = 0
        serve = 0

    elif s == "TAKE":
        take += 1
        count += 1
        if count == 1000:
            count = 1

    elif s == "SERVE":
        serve += 1