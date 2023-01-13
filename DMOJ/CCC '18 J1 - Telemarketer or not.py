first = int(input())
second = int(input())
third = int(input())
fourth = int(input())

if (
    (first == 9 or first == 8) 
    and (fourth == 9 or fourth == 8) 
    and (second == third)
    ) :
    print("ignore")
else :
    print("answer")