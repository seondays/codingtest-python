# https://dmoj.ca/problem/coci12c5p1

input = input()

input_list = input.split("|")
a_count = 0
c_count = 0

for i in input_list :
    if i[0] == "A" or i[0] == "E" or i[0] == "D":
        a_count += 1
    elif i[0] == "G" or i[0] == "C" or i[0] == "F" :
        c_count += 1

if a_count < c_count :
    print("C-dur")
elif a_count > c_count :
    print("A-mol")
    
    
elif a_count == c_count :
    
    if input_list[-1][-1] == "A" or input_list[-1][-1] == "E" or input_list[-1][-1] == "D":
        print("A-mol")
    else :
        print("C-dur")
        