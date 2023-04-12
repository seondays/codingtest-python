# https://dmoj.ca/problem/ccc13s1

# TODO : 입력 받은 내용 리스트로 가공하기

def change_str_to_int(input):
    '''문자열 타입인 숫자를 입력하면, 1을 더한 후 다시 문자열 타입으로 리턴합니다.'''
    return str(int(input) + 1)

year = change_str_to_int(input())

# TODO : 고유의 숫자인지 확인하기

def is_distinct_digits(list):
    '''리스트가 고유한 숫자만으로 이루어져 있는지 여부를 확인합니다.'''
    
    for i in list:
        if list.count(i) > 1:
            return False
    
    return True

is_distinct = False

while is_distinct is False:
    if is_distinct_digits(list(year)):
        is_distinct = True
    else:
        year = change_str_to_int(year)

print(year)
