# http://usaco.org/index.php?page=viewproblem2&cpid=1299

N, T = list(map(int,input().split()))
haybales = 0
days = []
delivery = []

for _ in range(N):
    day, count = list(map(int,input().split()))

    days.append(day)
    delivery.append(count)

days.append(T+1)
delivery.append(0)

result = 0
for i in range(N):
    haybales += delivery[i]
    if days[i+1] - days[i] < haybales:
        result += days[i+1] - days[i]
        haybales -= days[i+1] - days[i]
    else:
        result += haybales
        haybales = 0
    
print(result)