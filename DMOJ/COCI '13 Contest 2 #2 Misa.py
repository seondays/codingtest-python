# https://dmoj.ca/problem/coci13c2p2

# TODO : 입력 처리하기
input_text = input().split(" ")
row = int(input_text[0])
column = int(input_text[1])
original_matrix = []

for i in range(row):
    input_row = list(input())
    original_matrix.append(input_row)

# TODO : 악수할 수 있는 횟수 구하기
def handshake_counting(maxtrix,row,column):
    count = 0
    
    for i in range(1,row+1):
        for j in range(1,column+1):
            if maxtrix[i][j] == 'o':
                if maxtrix[i-1][j-1] == 'o':
                    count += 1              
                if maxtrix[i-1][j] == 'o':
                    count += 1                    
                if maxtrix[i-1][j+1] == 'o':
                    count += 1                
                if maxtrix[i][j-1] == 'o':
                    count += 1                    
                if maxtrix[i][j+1] == 'o':
                    count += 1                    
                if maxtrix[i+1][j-1] == 'o':
                    count += 1                
                if maxtrix[i+1][j] == 'o':
                    count += 1                    
                if maxtrix[i+1][j+1] == 'o':
                    count += 1
    return count // 2
    
# TODO : 상하좌우 추가 공간 만들기
def make_space(matrix,row,column):
    new_matrix = []
    for i in matrix:
        i.insert(0,'.')
        i.insert(len(i),'.')
        new_matrix.append(i)
    new_matrix.insert(0,list('.'*(column+2)))
    new_matrix.insert(row+1,list('.'*(column+2)))
    return new_matrix
    
    
# TODO : 앉을 자리가 있는지 여부 구하기
def check_handshake_available(maxtrix):
    for i in maxtrix:
        if '.' in i:
            return True
    return False
    
# TODO : main

handshake_count_list = []

if check_handshake_available(original_matrix):
    for i in range(row):
        for j in range(column):
            
            copy_matrix = [row[:] for row in original_matrix]
            
            if copy_matrix[i][j] == '.':
                copy_matrix[i][j] = 'o'
                matrix = make_space(copy_matrix,row,column)
                handshake_count_list.append(handshake_counting(matrix,row,column))
    print(max(handshake_count_list))
    
else:
    print(handshake_counting(make_space(original_matrix,row,column),row,column))