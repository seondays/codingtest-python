# https://dmoj.ca/problem/coci12c5p1

input = input().split("|")

a_count = 0
c_count = 0
last_tone = input[-1]

for i in input :

    if i[0] in ['A','D','E']:
        a_count += 1
    
    if i[0] in ['C','F','G']:
        c_count += 1
    
if a_count == c_count :
    if last_tone[-1] in ['A','D','E']:
        a_count += 1
    
    if last_tone[-1] in ['C','F','G']:
        c_count += 1
        
if a_count < c_count :
    print("C-dur")
elif a_count > c_count :
    print("A-mol")