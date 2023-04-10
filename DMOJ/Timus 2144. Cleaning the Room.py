# https://acm.timus.ru/problem.aspx?space=1&num=2144

# TODO : input을 이용하여 상자 리스트 만들기
def read_box(n):
    boxes = []
    for i in range(n):
        box = list(map(int,input().split(" ")))
        box.pop(0)
        boxes.append(box)
    return boxes

count = int(input())
boxes = read_box(count)

# TODO : 상자 내부가 차례대로 정리되어 있는지 확인



# TODO : 상자들이 차례대로 정리가 가능한지 확인
