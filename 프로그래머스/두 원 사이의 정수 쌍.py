import math

def solution(r1, r2):
    
    dot1 = 0
    dot2 = 0
    
    for i in range(r2):
        y = math.floor(math.sqrt(r2*r2-i*i))
        dot2 += y
    
    for i in range(r1):
        y = math.floor(math.sqrt(r1*r1-i*i))
        if y == math.sqrt(r1*r1-i*i):
            dot1 += -1
        dot1 +=y
    
    answer = (dot2-dot1)*4
    return answer