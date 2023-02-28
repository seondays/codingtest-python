# https://dmoj.ca/problem/coci08c3p2

string = input()
v = ["a","e","i","o","u"]
i = 0
result = ""

# zepelepenapa papapripikapa -> zelena paprika

while i < len(string):
    if string[i] in v :
        result += string[i]
        i += 3
    else :
        result += string[i]
        i += 1

print(result)



