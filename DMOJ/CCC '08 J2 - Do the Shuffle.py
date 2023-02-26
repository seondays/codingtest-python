# https://dmoj.ca/problem/ccc08j2

button = 0
music = "ABCDE"

while button != 4 :
    button = int(input())
    count = int(input())

    for i in range(0,count):

        if button == 1 :
            music = music[1:5] + music[0]

        if button == 2 :
            music = music[-1] + music[0:4]
    
        if button == 3:
            music = music[1] + music[0] + music[2:5]

for i in music:
    print(i,"",end="")