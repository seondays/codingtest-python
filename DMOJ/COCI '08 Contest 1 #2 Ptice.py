#https://dmoj.ca/problem/coci08c1p2

count = int(input())
sequence = input()

adrian = "ABC" * count
bruno = "BABC" * count
goran = "CCAABB" * count

print(bruno)

adrian_count = 0
bruno_count = 0
goran_count = 0

for i in range(count):
    if sequence[i] == adrian[i]:
        adrian_count += 1
    if sequence[i] == bruno[i]:
        bruno_count += 1
    if sequence[i] == goran[i]:
        goran_count += 1
    
max_value = max(adrian_count,bruno_count,goran_count)

print(max_value)
if adrian_count == max_value :
    print("Adrian")
if bruno_count == max_value :
    print("Bruno")
if goran_count == max_value :
    print("Goran")