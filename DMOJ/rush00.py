# 5,3
DASH = '-'
CORNER = 'o'
SIDE = '|'

x,y = 10,10

# y번만큼 행 출력 반복
for i in range(y):
    # 첫번째 행과 마지막 행인 경우 처리
    if (i == 0 or i == y-1):
        print(CORNER, end='')
        print(DASH * (x-2), end='')
        # x가 1인 경우 처리하기
        if (x != 1):
            print(CORNER)
        else:
            print()
    # 중간 행인 경우
    else:
        print(SIDE, end='')
        print(' ' * (x-2),end='')
        # x가 1인 경우 처리하기
        if (x != 1):
            print(SIDE)
        else:
            print()
    