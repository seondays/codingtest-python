# https://dmoj.ca/problem/ecoo19r2p1

# 이메일에 +가 포함되어 있는지 체크하기
def is_plus_in_email(email):
    if "+" in email:
        return True
    return False

# + 부터 @ 바로 이전까지의 값을 제거한 새로운 이메일 반환하기
def delete_suffix(email):
    plus_index = email.index("+")
    at_index = email.index("@")

    new_email = email[:plus_index] + email[at_index:]

    return new_email

# 대문자를 소문자로 바꿔준 새로운 이메일 반환하기
def lower_email(email):
    new_email = email.lower()

    return new_email

# 아이디에 존재하는 점을 제거한 새로운 이메일 반환하기
def delete_dot(email):
    at_index = email.index("@")
    id = email[:at_index].replace(".","")

    new_email = id + email[at_index:]

    return new_email

#main
for i in range(10):
    n = int(input())
    email_list = []
    
    for j in range(n):
        email = input()

        if is_plus_in_email(email):
            email = delete_suffix(email)
        email = lower_email(email)
        email = delete_dot(email)
        email_list.append(email)

    email_set = set(email_list)

    print(len(email_set))