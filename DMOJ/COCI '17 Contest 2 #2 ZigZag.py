# https://dmoj.ca/problem/coci17c2p2

n = list(map(int,input().split()))
words_n = n[0]
letters_n = n[1]

# 첫글자:단어 리스트 딕셔너리와, 첫글자:단어 리스트 인덱스 딕셔너리 만들기 
letters = {}
words_idx = {}

words_lst = []
for i in range(words_n):
    word = input()

    words_lst.append(word)

letters_lst = []
for i in range(letters_n):
    letter = input()

    letters_lst.append(letter)

    if letter not in letters:
        letters[letter] = []
    
    if letter not in words_idx:
        words_idx[letter] = 0

for i in words_lst:
    if i[0] in letters:
        letters[i[0]].append(i)

# 단어 리스트 알파벳 오름차순으로 정렬
for v in letters.values():
    v.sort()

# 출력 로직
for i in range(letters_n):
    v = letters_lst[i]

    print(letters[v][words_idx[v]])

    if words_idx[v] == len(letters[v]) - 1:
        words_idx[v] = 0
    else:
        words_idx[v] += 1