# https://dmoj.ca/problem/ccc20j2

max_people = int(input())
patient = int(input())
contagion = int(input())

day = 0
count_people = patient

while count_people <= max_people:
    count_people += patient * contagion

    patient = patient * contagion

    day += 1
    
print(day)