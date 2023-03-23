# https://dmoj.ca/problem/ecoo19r1p1

for j in range(10):

    first_line = input().split(" ")

    shirts = int(first_line[0])
    event_days = int(first_line[1])
    entire_days = int(first_line[2])

    second_line = input().split(" ")
    event_days_list = [int(i) for i in second_line]

    count = 0
    entire_shirts = shirts

    for i in range(1,entire_days+1):

        if shirts == 0 :
            count += 1
            shirts = entire_shirts

        shirts -= 1
        
        # 하루에도 1건 이상 이벤트가 발생할 수 있기 때문에 이를 고려해야 한다
        if event_days_list.count(i) == 1:
            shirts += 1
            entire_shirts += 1
        if event_days_list.count(i) > 1 :
            shirts += event_days_list.count(i)
            entire_shirts += event_days_list.count(i)

    print(count)
