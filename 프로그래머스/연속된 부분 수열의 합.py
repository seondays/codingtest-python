def solution(sequence, k):
    
    answer = []
    sum = 0
    right = 0
    
    for i in range(len(sequence)):
        while sum < k and right < len(sequence):
            sum += sequence[right]
            right += 1
        
        if sum == k:
            answer.append([i,right-1,right-i-1])
        
        sum -= sequence[i]
        
    answer = sorted(answer,key = lambda x : x[2])
    answer = [answer[0][0],answer[0][1]]
    return answer