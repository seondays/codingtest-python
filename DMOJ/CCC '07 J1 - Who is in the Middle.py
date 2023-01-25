# https://dmoj.ca/problem/ccc07j1

first = int(input())
second = int(input())
third = int(input())

if first < second :
    if first < third :
        if second < third :
            print(second)
        else :
            print(third)
    else :
        print(first)
elif first > second :
    if second < third :
        if first < third :
            print(first)
        else :
            print(third)
    else :
        print(second)