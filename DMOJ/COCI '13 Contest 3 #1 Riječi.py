# https://dmoj.ca/problem/coci13c3p1

pressing_count = int(input())

start = "A"

for i in range(0,pressing_count) :
    answer = ""
    for j in start :
        if j == "A" :
            answer += "B"
        elif j == "B" :
            answer += "BA"
    
    start = answer

a_count = answer.count("A")
b_count = answer.count("B")

print(a_count, b_count)