# http://usaco.org/index.php?page=viewproblem2&cpid=1299

N, T = list(map(int,input().split()))
haybales = 0
days = []
delivery = []

for _ in range(N):
    day, count = list(map(int,input().split()))

    days.append(day)
    delivery.append(count)

print(days)
print(delivery)