#https://dmoj.ca/problem/ecoo17r3p1

for i in range(10):

    store_and_days = input().split(" ")

    store = int(store_and_days[0])
    day = int(store_and_days[1])

    metrix = []

    for i in range(day):
        row = input().split(" ")
        for j in range(store):
            row[j] = int(row[j])
        metrix.append(row)

    bouns = 0

    for i in metrix:
        if sum(i) % 13 == 0:
            bouns += sum(i)//13
        
    for i in range(store):
        total = 0
        for j in range(day):
            total += metrix[j][i]
        
        if total % 13 == 0:
            bouns += total // 13

    print(bouns)