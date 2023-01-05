# https://dmoj.ca/problem/ccc19j1

first_team_score_3 = int(input())
first_team_score_2 = int(input())
first_team_score_1 = int(input())
second_team_score_3 = int(input())
second_team_score_2 = int(input())
second_team_score_1 = int(input())

def calculate_score(first,second,thrid):
    score = first * 3 + second * 2 + thrid
    return score

if calculate_score(first_team_score_3,first_team_score_2,first_team_score_1) > calculate_score(second_team_score_3,second_team_score_2,second_team_score_1):
    print("A")
elif calculate_score(first_team_score_3,first_team_score_2,first_team_score_1) < calculate_score(second_team_score_3,second_team_score_2,second_team_score_1):
    print("B")
else :
    print("T")
    