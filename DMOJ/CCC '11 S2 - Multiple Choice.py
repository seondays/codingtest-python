# https://dmoj.ca/problem/ccc11s2

test_count = int(input())
correct_answers = []
student_answers = []
correct_count = 0

for i in range(test_count) :
    student_answer = input()
    
    student_answers.append(student_answer)
      
for i in range(test_count) :
    correct_answer = input()
    
    correct_answers.append(correct_answer)
    
for i in range(test_count) :
    if correct_answers[i] == student_answers[i] :
        correct_count += 1
    
print(correct_count)
    