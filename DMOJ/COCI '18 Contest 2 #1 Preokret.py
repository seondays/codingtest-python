# https://dmoj.ca/problem/coci18c2p1

A_goal_count = int(input())
A_goal_list = []

for i in range(A_goal_count):
    goal_time = int(input())
    A_goal_list.append(goal_time)

B_goal_count = int(input())
B_goal_list = []

for i in range(B_goal_count):
    goal_time = int(input())
    B_goal_list.append(goal_time)

goal_in_first_halfTime = 0
turnaround = 0
A_score = 0
B_score = 0
winning = ""

for i in range(1,1440*2):
    if i in A_goal_list:
        A_score += 1
    elif i in B_goal_list:
        B_score += 1
        
    if A_score == 0 and B_score == 0:
        if B_score > A_score:
            winning = "B"
        elif B_score < A_score:
            winning = "A"
        
    if B_score > A_score:
        if winning == "A":
            turnaround += 1
        winning = "B"
    if A_score > B_score:
        if winning == "B":
            turnaround += 1
        winning = "A"
    
    if i == 1440 :
        print(A_score + B_score)

print(turnaround)
    
