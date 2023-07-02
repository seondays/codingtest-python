# https://dmoj.ca/problem/coci15c2p1

keyboard_dict = {'a':2,'b':2,'c':2,'d':3,'e':3,'f':3,
                 'g':4,'h':4,'i':4,'j':5,'k':5,'l':5,
                 'm':6,'n':6,'o':6,'p':7,'r':7,'q':7,'s':7,
                 't':8,'u':8,'v':8,'w':9,'x':9,'y':9,'z':9
                 }

# input 입력 받기
n = int(input())
answer = 0
words = []

for i in range(n):
    word = input()
    words.append(word)

keys = str(input())

# 단어를 키보드 누르는 순서(숫자)로 변환하기
words_num = []

for i in words:
    str_to_num = ""
    for k in i:
        str_to_num += str(keyboard_dict[k])
    
    if keys == str_to_num:
        answer += 1

print(answer)