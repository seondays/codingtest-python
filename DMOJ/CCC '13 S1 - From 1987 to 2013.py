# https://dmoj.ca/problem/ccc13s1

# TODO : 입력 받은 내용 리스트로 가공하기

def change_str_to_int(input):
    '''문자열 타입인 숫자를 입력하면, 1을 더한 후 다시 문자열 타입으로 리턴합니다.'''
    return str(int(input) + 1)

year = change_str_to_int(input())

# TODO : 고유의 숫자인지 확인하기
