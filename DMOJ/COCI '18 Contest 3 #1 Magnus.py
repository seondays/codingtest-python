# https://dmoj.ca/problem/coci18c3p1

sentence = input()
honi_count = 0
honi_dictionary = "HONI"
answer = 0

for i in sentence:
    if i == honi_dictionary[honi_count]:
        honi_count += 1

    if honi_count == 4 :
        answer += 1
        honi_count = 0

print(answer)
