# https://dmoj.ca/problem/ecoo18r1p1

for j in range(10) :
    input_data = input().split(" ")

    playing_days = int(input_data[0])
    next_days = int(input_data[1])

    habits = [input() for i in range(next_days)]
    willow_playing = 0

    for i in habits:
        if i == "B":
            willow_playing += playing_days
            
        if willow_playing > 0:
            willow_playing -= 1

    print(willow_playing)
