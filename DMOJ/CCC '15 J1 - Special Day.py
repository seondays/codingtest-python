# https://dmoj.ca/problem/ccc15j1

month = int(input())
day = int(input())

special_month = 2
special_day = 18

if month == special_month and day == special_day :
    print("Special")
elif month < special_month :
    print("Before")
elif month > special_month :
    print("After")
elif day < special_day :
    print("Before")
elif day > special_day :
    print("After")