# https://dmoj.ca/problem/ecoo17r1p1

COST = [12,10,7,5]

for i in range(0,10):
    price = int(input())

    students = input().split(" ")

    numbers_of_all_students = int(input())

    for i in range(0,len(students)):
        students[i] = float(students[i])
    
    grade_level_students = []
    
    for i in students:
        grade_level_students.append(int(i * numbers_of_all_students))
    
    if sum(grade_level_students) != numbers_of_all_students:
        difference = numbers_of_all_students - sum(grade_level_students)
        max_grade = students.index(max(students))
        grade_level_students[max_grade] = grade_level_students[max_grade] + difference
    
    final_cost = 0

    for i in range(0,4):
        final_cost += COST[i] * grade_level_students[i]
    
    if final_cost / 2 < price:
        print("YES")
    else:
        print("NO")