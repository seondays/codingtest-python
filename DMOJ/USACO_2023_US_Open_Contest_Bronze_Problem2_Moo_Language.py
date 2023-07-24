# http://usaco.org/index.php?page=viewproblem2&cpid=1324

# nouns, transitive verbs, intransitive verbs, and conjunctions
# periods and commas
# 마침표나 쉼표는 단어 뒤에 나오는 경우 단어의 바로 뒤에 나와야 함
# 그 다음에 다른 단어가 다시 나올 경우 공백이 들어가야 함
# 문장의 형식 :
# nouns + interansitive verbs
# nouns + transitive verbs + nouns
# 타동사를 사용하는 경우 하나 이상의 명사가 타동사 뒤에 와야 함
# 하나 이상의 명사가 타동사 뒤에 오는 경우, 명사들은 쉼표로 구분됨 (a, b, c, d)
# 문장과 문장 사이에 접속사가 있는 문장은 또 다른 문장들과 접속사로 결합할 수 없음
# 모든 문장은 마침표로 끝나야 함

# 주어진 인풋들을 명사 타동사 자동사 접속사로 분류하기
# 먼저 자동사와 명사로 문장 만들기 (명사, 자동사, 마침표가 1개씩 필요)
# 문장을 만들 수 있는 구성 요소가 충분하지 않을 경우 pass
# 타동사 1개당 명사 2개씩 분배하기
    # 남은 구성요소들 중 타동사 1개당 명사 2개가 되지 않을 경우 체크
        # 온전한 타동사 문장이 있다면 남은 명사는 해당 타동사 문장에 쉼표를 사용하여 연결
            # 쉼표 개수가 부족하다면 pass
# 문장과 문장을 연결하는 접속사는 최대한 다 사용해야 함
    # 단, 이미 완성된 문장들을 연결하고자 하는 경우 일부 마침표를 제거해야 함(기존 마침표 개수-1)
    # 남은 구성요소들 중 문장의 개수가 접속사 1개당 2개가 되지 않을 경우 체크해서 pass

def save_words(word,type,words_dict):
    words_dict[type].append(word)

# main
count = int(input())

for i in range(count):
    words_dict = {"noun":[],"transitive-verb":[],"intransitive-verb":[],"conjunction":[]}
    n = list(map(int,input().split()))

    word_number = n[0]
    period = n[1]
    comma = n[2]

    for k in range(word_number):
        sentence = input().split()
        word = sentence[0]
        type = sentence[1]

        save_words(word,type,words_dict)

    noun_index = len(words_dict["noun"])
    intran_index = len(words_dict["intransitive-verb"])
    tran_index = len(words_dict["transitive-verb"])
    con_index = len(words_dict["conjunction"])
    lst = []

    # 자동사 개수 확인
    while intran_index > 0 and noun_index > 0:
        s = []
        s.append(words_dict["noun"][noun_index-1])
        s.append(words_dict["intransitive-verb"][intran_index-1])
        s.append(".")

        lst.append(s)

        noun_index -= 1
        intran_index -= 1
        period -= 1

    while tran_index > 0 and noun_index > 1:
        if tran_index == 1 and noun_index > 1:
            s = []

            s.append(words_dict["noun"][noun_index-1])
            s.append(words_dict["transitive-verb"][tran_index-1])
            
            noun_index -= 1

            for i in range(noun_index):
                if i == noun_index:
                    s.append(words_dict["noun"][noun_index-1])

                else:
                    s.append(words_dict["noun"][noun_index-1]+",")
                
                noun_index -= 1
            
            s.append(".")
            period -= 1
            lst.append(s)
            break

        s = []

        s.append(words_dict["noun"][noun_index-1])
        s.append(words_dict["transitive-verb"][tran_index-1])
        s.append(words_dict["noun"][noun_index-2])
        s.append(".")

        lst.append(s)

        noun_index -= 2
        tran_index -= 1
        period -= 1

    result = []

    # 접속사 처리

    for i in range(0,len(lst)):
        if i % 2 == 0 :
            result.append(lst[i])
        elif i % 2 == 1 and con_index > 0:
            result.append(words_dict["conjunction"][con_index-1])
            con_index -= 1
            period += 1
            result.append(lst[i])
        else:
            result.append(lst[i])
    
    for i in range(len(result)):
        if result[i] in words_dict["conjunction"]:
            result[i-1] = result[i-1][:-1]

    # 단어개수 세기
    count = 0
    for word in result:
        if isinstance(word,list):
            count += len(word)
            if '.' in word:
                count -= 1
        else:
            count+= 1
    
    print(count)


    # 출력하기
    
    for i in range(len(result)):
        if isinstance(result[i],list):
            if len(result)-1 == i:
                for k in range(len(result[i])):
                    if result[i][-1] ==  '.':
                        if k == len(result[i])-2:
                            print(result[i][k],end='')
                        else:
                            if result[i][k] == '.':
                                print(result[i][k],end='')
                            else:
                                print(result[i][k],end=' ')
            else:
                for k in range(len(result[i])):
                    if result[i][-1] ==  '.':
                        if k == len(result[i])-2:
                            print(result[i][k],end='')
                        else:
                            print(result[i][k],end=' ')
                    else:
                        print(result[i][k],end=' ')
        else:
            print(result[i],end=' ')
    print()