# https://dmoj.ca/problem/coci20c2p1

#입력 처리
days = int(input())
characters = input()

#기본 그래프 틀 그리기
matrix = []

for i in range(2*(days + 1)):
    dot_list = list('.'*days)
    matrix.append(dot_list)

#그래프 내용 작성하기
col = days + 1

for i in range(len(characters)):
    if characters[i] == '+':
        matrix[col][i] = '/'
        col += 1
    if characters[i] == '-':
        col -= 1
        matrix[col][i] = '\\'
    if characters[i] == '=':
        matrix[col][i] = '_'

# main
for i in range(len(matrix)-1,-1,-1):
    if matrix[i].count('.') != days:
        print(''.join(matrix[i]))
    
    




        
