# http://usaco.org/index.php?page=viewproblem2&cpid=1325

# 소 리스트 만들기
def make_cows(n):
    cows = [i for i in range(n)]
    return cows

# 활성 리스트에서 다음으로 이동할 정보를 저장하기
def make_next_position_dict(active_n,active):
    dict = {}

    for i in range(active_n):
        if i == active_n-1:
            dict[active[i]] = active[0]
        else:
            dict[active[i]] = active[i+1]
    return dict

# 시간 진행에 따라 활성 리스트 증가시키기
def increasing_active_list(active,cows_n):
    return [0 if active[i] == cows_n-1 else active[i]+1 for i in range(len(active))]

# 활성 리스트대로 소들의 위치 변경하기
def moving_cows(cows,cows_n,active_dict,active):
    dacing_cows = [0] * cows_n

    for i in range(cows_n):
        if i in active:
            dacing_cows[active_dict[i]] = cows[i]
        else:
            dacing_cows[i] = cows[i]
    return dacing_cows

# main
cows_n, active_n, times = list(map(int,input().split()))
active = list(map(int,input().split()))

cows = make_cows(cows_n)

for i in range(times):
    active_dict = make_next_position_dict(active_n,active)

    cows = moving_cows(cows,cows_n,active_dict,active)
    active = increasing_active_list(active,cows_n)

print(*cows)
