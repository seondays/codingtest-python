# https://dmoj.ca/problem/coci06c5p1

ball = 1
movement = input()

def movingA(ball) :
    if ball == 1 :
        ball = 2
    elif ball == 2 :
        ball = 1
    
    return ball
        
def movingB(ball) :
    if ball == 2 :
        ball = 3
    elif ball == 3 :
        ball = 2
    
    return ball
        
def movingC(ball) :
    if ball == 1 :
        ball = 3
    elif ball == 3 :
        ball = 1
    
    return ball
        

for i in movement :
    if i == "A" :
        ball = movingA(ball)
    elif i == "B":
        ball = movingB(ball)
    elif i == "C":
        ball = movingC(ball)
        
print(ball)