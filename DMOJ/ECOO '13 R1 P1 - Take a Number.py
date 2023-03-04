# https://dmoj.ca/problem/ecoo13r1p1

count = int(input())

take = 0
serve = 0

while True:
    status = input()
    if status == "EOF":
        break

    if status == "CLOSE":
        print(take,(take-serve),count)
        take = 0
        serve = 0

    if status == "TAKE":
        take += 1
        count += 1
        if count == 1000:
            count = 1
    
    if status == "SERVE":
        serve += 1