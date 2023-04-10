# https://acm.timus.ru/problem.aspx?space=1&num=2144

def read_box(n):
    boxes = []
    for i in range(n):
        box = list(map(int,input().split(" ")))
        box.pop(0)
        boxes.append(box)
    return boxes

def is_box_sorted(boxes):
    for i in range(len(boxes)):
        if boxes[i] != sorted(boxes[i]):
            return False
    return True

def make_list_start_end_in_box(boxes):
    new_list = []
    for i in range(len(boxes)):
        list = []
        list.append(boxes[i][0])
        list.append(boxes[i][-1])
        new_list.append(list)
    return sorted(new_list)

def is_boxes_sorted(boxes):
    for i in range(len(boxes)-1):
        if boxes[i][-1] > boxes[i+1][0]:
            return False
    return True

# Main Program

count = int(input())
boxes = read_box(count)

if is_box_sorted(boxes):
    if is_boxes_sorted(make_list_start_end_in_box(boxes)):
        print("YES")
    else:
        print("NO")
else:
    print("NO")