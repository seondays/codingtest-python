def solution(arr):
    result = []
    s = set(arr)
    
    for i in s:
        if len(arr) == len(s):
            return [-1]
        counter = arr.count(i)
        if not counter == 1:
            result.append(counter)    
    
    return result

#test
print(solution([1,2,3,3,3,3,4,4]))
print(solution([3,2,4,4,2,5,2,5,5]))
print(solution([3,5,7,9,1]))