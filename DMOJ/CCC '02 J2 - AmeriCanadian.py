#https://dmoj.ca/problem/ccc02j2

text = input()
text_list = []
vowels = ["a","e","i","o","u","y"]

while text != "quit!":
    if text[-2:] == "or" and len(text) > 4 and (text[-3:-2] not in vowels) :
        text_list.append(text[:-2]+"our")
    else:
        text_list.append(text)
    
    text = input()

for i in text_list:
    print(i)