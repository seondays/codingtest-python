# http://usaco.org/index.php?page=viewproblem2&cpid=1323

input_n = int(input())
input_text = input()

# 패턴 적용을 위해 문자열을 작은 구간들로 쪼개기
message_index = [i for i in range(len(input_text)) if input_text[i] != 'F']

min_range = 0
max_range = 0

# 쪼갠 구간들에서 연속문자 최소개수, 최대개수를 구하기
for i,k in zip(message_index,message_index[1:]):
    # 시작과 끝이 같고, 짝수이면
    if (k-i+1) % 2 == 0 and input_text[i] == input_text[k]:
        min_range += 1
    
    # 시작과 끝이 다르고, 홀수이면
    elif (k-i+1) % 2 != 0 and input_text[i] != input_text[k]:
        min_range += 1
    
    # 시작 끝이 같으면 최대값은 n-2
    if input_text[i] == input_text[k]:
        max_range += k-i
    # 시작 끝이 다르면 최대값은 n-2
    elif input_text[i] != input_text[k]:
        max_range += k-i-1

# 문자열의 시작/끝이 F로 시작한다면 개수 체크하기
count_f = input_n - message_index[-1] - 1 + message_index[0]

# 최소개수, 최대개수 사이의 정답들 출력하기
result = []
for i in range(min_range,max_range+count_f+1,1+(count_f == 0)):
    result.append(i)

print(len(result))
print(*result,sep='\n')