# http://usaco.org/index.php?page=viewproblem2&cpid=891

input_file = open('shell.in','r')
output_file = open('shell.out','w')

n = int(input_file.readline().strip())
round = [[int(j) for j in i.split()] for i in input_file.read().strip().split('\n')]

def set_round(n):
    setting = [0,0,0]
    setting[n-1] = 1
    return setting

def play_round(swap,answer_now):
    result = answer_now
    result[swap[1]-1],result[swap[0]-1] = result[swap[0]-1],result[swap[1]-1]
    return result

def check_answer(answer,predict):
    if answer[predict-1] :
        return True
    return False

# main
score_list = []
for i in range(1,4):
    score = 0
    setting = set_round(i)
    for j in round:
        swap = j[0:2]
        predict = j[-1]
        round_result = play_round(swap,setting)
        if check_answer(round_result,predict):
            score += 1
    score_list.append(score)

output_file.write(str(max(score_list)))