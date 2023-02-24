# https://dmoj.ca/problem/ccc20j2

limit = int(input())
first_patient = int(input())
infectious = int(input())

day = 0
today = first_patient
count = first_patient

while count <= limit :
    day += 1
    
    today = today * infectious
    
    count += today
    
print(day)

