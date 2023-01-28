# https://dmoj.ca/problem/coci18c3p1

word_input = input()
honi_counter = 0
result = 0

for i in word_input :
    i.upper()
    
    if honi_counter == 0 and i == "H" :
        honi_counter += 1
    elif honi_counter == 1 and i == "O" :
        honi_counter += 1
    elif honi_counter == 2 and i == "N" :
        honi_counter += 1
    elif honi_counter == 3 and i == "I" :
        honi_counter = 0
        result += 1

print(result)