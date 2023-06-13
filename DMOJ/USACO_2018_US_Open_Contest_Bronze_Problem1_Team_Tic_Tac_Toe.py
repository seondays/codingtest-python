# http://usaco.org/index.php?page=viewproblem2&cpid=831

input_file = open('tttt.in','r')
ouput_file = open('tttt.out','w')
play_board = input_file.read().strip().split('\n')

# 승리팀 계산하기
def check_count_row_winner(play_board):
    for i in play_board:
        if len(set(i)) == 2:
            print(set(i))
            if set(i) not in winner_team:
                winner_team.append(set(i))
        if len(set(i)) == 1:
            if set(i) not in winner_cow:
                winner_cow.append(set(i))

# 세로 비교list 만들기
def make_col_list(play_board):
    new_board = [''] * len(play_board)
    for i in range(len(play_board)):
        for j in range(len(play_board)):
            new_board[j] = new_board[j] + play_board[i][j]

    return new_board    
        
# 대각선 비교list 만들기
def make_diagonal_list(play_board):
    first_diagonal = ['']
    second_diagonal = ['']
    
    for i in range(len(play_board)):
        first_diagonal[0] = first_diagonal[0] + play_board[i][i]
        second_diagonal[0] = second_diagonal[0] + play_board[i][len(play_board)-1-i]
    
    result = []
    result.append(first_diagonal)
    result.append(second_diagonal)

    return result

#main
winner_cow = []
winner_team = []
diagonal = make_diagonal_list(play_board)[0]
antiMdiagonal = make_diagonal_list(play_board)[1]

row_result = check_count_row_winner(play_board)

col_result = check_count_row_winner(make_col_list(play_board))

diagonal_result = check_count_row_winner(diagonal)

antiMdiagonal_result = check_count_row_winner(antiMdiagonal)

ouput_file.write(str(len(winner_cow))+'\n')
ouput_file.write(str(len(winner_team)))


