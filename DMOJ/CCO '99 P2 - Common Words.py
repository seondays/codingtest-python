# https://dmoj.ca/problem/cco99p2

# 딕셔너리에 문자 추가하기
def add_words(words, word):
    if word in words:
        words[word] += 1
    else:
        words[word] = 1

    return words

# 딕셔너리 값을 키로 변경하기
def reverse_key_value(words):
    result = {}

    for i in list(set(words.values())):
        lst = []
        for k,v in words.items():
            if v == i:
                lst.append(k)
        result[i] = lst
    
    return result

# 요구되는 출현 빈도수에 해당되는 단어 구하기
def get_common_rate(words, rate):
    keys = sorted(words.keys(),reverse=True)
    total = 0

    for i in range(len(keys)):
        if total + len(words[keys[i]]) >= rate:
            if total == rate-1 and i < len(keys):
                return words[keys[i]]
            else:
                return []
        total += len(words[keys[i]])

# 빈도별로 제목 출력하기
def print_title(rate):
    s = str(rate)
    if s[-1] == '1' and s[-2:] != "11":
        print(s + "st most common word(s):")
    elif s[-1] == '2' and s[-2:] != "12":
        print(s + "nd most common word(s):")
    elif s[-1] == '3' and s[-2:] != "13":
        print(s + "rd most common word(s):")
    else:
        print(s + "th most common word(s):")

# main 
total_count = int(input())

for i in range(total_count):
    round_lst = list(map(int,input().split()))
    round_num = round_lst[0]
    rate = round_lst[1]
    words = {}

    for j in range(round_num):
        word = input()
        words = add_words(words,word)

    words = reverse_key_value(words)

    result =get_common_rate(words,rate)
    print_title(rate)
    if result:
        print(*result,sep="\n")
        print()
    else:
        print()
