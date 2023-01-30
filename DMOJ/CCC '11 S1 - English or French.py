# https://dmoj.ca/problem/ccc11s1

line_input = int(input())

t_count = 0
s_count = 0

for i in range(line_input) :
    text = input().upper()
    
    t_count += text.count("T")
    s_count += text.count("S")
    
if s_count < t_count :
    print("English")
elif t_count <= s_count :
    print("French")