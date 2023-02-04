# https://dmoj.ca/problem/coci13c3p1

pressing_count = int(input())

# A -> B -> BA -> BAB -> BABBA

a_count = 1
b_count = 0


for i in range(0,pressing_count) :
    answer_a = a_count
    answer_b = b_count
    
    a_count = answer_b
    b_count = answer_b+answer_a

print(a_count, b_count)
