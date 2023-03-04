#https://dmoj.ca/problem/ecoo15r1p1

seconds = 0
orange = 0
blue = 0
green = 0
yellow = 0
pink = 0
violet = 0
brown = 0

for j in range(0,10) :

    while True:
        color = input()

        if color == "red":
            seconds += 16
        if color == "orange":
            orange += 1
        if color == "blue":
            blue += 1
        if color == "green":
            green += 1
        if color == "yellow":
            yellow += 1
        if color == "pink":
            pink += 1
        if color == "violet":
            violet += 1
        if color == "brown":
            brown += 1
        if color == "end of box":
            break

    for i in [orange,blue,green,yellow,pink,violet,brown]:
        if i <= 7 :
            seconds += 13
        
        if i > 7 :
            seconds += (i//7) * 13
            if i % 7 != 0:
                seconds += 13

    print(seconds)

    orange = 0
    blue = 0
    green = 0
    yellow = 0
    pink = 0
    violet = 0
    brown = 0
    seconds = 0