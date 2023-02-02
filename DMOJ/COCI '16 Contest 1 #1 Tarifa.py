# https://dmoj.ca/problem/coci16c1p1

data = int(input())
month = int(input())
excess = 0

for i in range(0,month) :
    use_data = int(input())
    
    excess += data - use_data
    
print(excess+data)
    