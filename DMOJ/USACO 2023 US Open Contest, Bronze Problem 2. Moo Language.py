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