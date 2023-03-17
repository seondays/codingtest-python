# https://dmoj.ca/problem/coci18c2p1

teamA_count = int(input())

teamA_times = []
teamB_times = []

for i in range(teamA_count):
    score_time = int(input())
    
    teamA_times.append(score_time)
    
teamB_count = int(input())

for i in range(teamB_count):
    score_time = int(input())
    
    teamB_times.append(score_time)

teamA_score = 0
teamB_score = 0
winner = ""
turnaround_count = 0

for i in range(2280):
    if i in teamA_times:
        teamA_score += 1
    
    if i in teamB_times:
        teamB_score += 1
        
    if teamA_score > teamB_score:
        
        if winner == "A":
            pass
        elif winner == "B":
            turnaround_count += 1
            winner = "A"
        elif winner == "":
            winner = "A"
            
    elif teamA_score < teamB_score:
        if winner == "A":
            turnaround_count += 1
            winner = "B"
        elif winner == "B":
            pass
        elif winner == "":
            winner = "B"
    
    if i == 1440:
        print(teamA_score+teamB_score)

print(turnaround_count)