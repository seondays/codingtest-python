# https://dmoj.ca/problem/ccc06s2

# 입력 받기
plaintext = input()
ciphertext = input()
encrypted = input()

plaintext_lst = []
ciphertext_lst = []

for i in plaintext:
    plaintext_lst.append(i)

for i in ciphertext:
    ciphertext_lst.append(i)

# 평문과 암호문 세트를 가지고 암호 해독 사전 만들기
def make_decrypt_dict(plaintext,ciphertext):
    result = {}

    for i in range(len(plaintext)):
        if ciphertext[i] not in result:
            result[ciphertext[i]] = plaintext[i]
    
    return result

# 주어진 암호문 해독하기
def decrypt(ciphertext,dectrypt_dict):
    result = ""
    ciphertext_lst = []

    for i in ciphertext:
        ciphertext_lst.append(i)

    for i in range(len(ciphertext_lst)):
        if ciphertext_lst[i] not in dectrypt_dict:
            result += "."
        else:
            result += dectrypt_dict[ciphertext_lst[i]]
    
    return result

# main
decrypt_dict = make_decrypt_dict(plaintext_lst,ciphertext_lst)
print(decrypt(encrypted,decrypt_dict))