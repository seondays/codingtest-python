# https://dmoj.ca/problem/ecoo18r1p2


for i in range(10):

    count = int(input())
    routes = []

    for i in range(count):
        route = [int(i) for i in input().split(" ")]
        routes.append(route)

    min_value = float("inf")

    for i in routes:
        now_min = int(min(i[2:]))
        
        if now_min < min_value:
            min_value = now_min

    check = []

    for i in routes:
        if min_value in i[2:]:
            check.append(i[0])

    check_sort = ",".join((map(str,sorted(check))))

    print(min_value,'{'+check_sort+'}')


    



