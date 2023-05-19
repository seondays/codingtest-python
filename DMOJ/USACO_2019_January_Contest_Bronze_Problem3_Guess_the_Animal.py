# http://usaco.org/index.php?page=viewproblem2&cpid=893

input_file = open('DMOJ/guess.in','r')
output_file = open('DMOJ/guess.out','w')

total_n = int(input_file.readline().strip())

# 특징 갯수 구하기
characteristics_list = []
characteristics_dict = {}

for i in input_file.read().strip().split('\n'):
    character = i.split()[2:]
    characteristics_list.append(character)

# 가장 빈도수가 많은 특징이 있는 경우의 수 출력하기
def solution(lst):

    if len(lst) == 1:
        return lst

    characteristics_dict = {}

    for i in lst:
        for j in i:
            if j in characteristics_dict:
                characteristics_dict[j] += 1
            else:
                characteristics_dict.setdefault(j,0)

    max_value = max(characteristics_dict.values())
    have_max_value = []

    for k,v in characteristics_dict.items():
        if v == max_value:
            have_max_value.append(k)
    return have_max_value


# 맥스벨류를 입력받아서 해당 값을 제거한 리스트 반환받기
def make_max_value(v,lst):
    new_char_list = []
    for i in lst:
        if v in i:
            i.remove(v)
            if len(i) == 0:
                continue
            new_char_list.append(i)
    return new_char_list
  

#main
# 맥스값 구하자
copy_characteristics_list = [list(sublist) for sublist in characteristics_list]
result_list = []
max_value = solution(characteristics_list) #[A,C]
for i in max_value:
    count = 1
    copy_characteristics_list = [list(sublist) for sublist in characteristics_list]
    while True:
        count += 1
        copy_characteristics_list = make_max_value(i,copy_characteristics_list) # 기존 리스트에서 A값을 제거한 리스트가 나옴
        if len(copy_characteristics_list) <= 1 :
            result_list.append(count)
            break
        max_value = solution(copy_characteristics_list) # A값을 제거한 리스트에서 또 맥스값을 구한다.

output_file.write(str(max(result_list)))


