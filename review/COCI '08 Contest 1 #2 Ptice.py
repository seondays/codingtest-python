#https://dmoj.ca/problem/coci08c1p2

adrian = "ABC"
bruno = "BABC"
goran = "CCAABB"

times = int(input())
text = input()

adrian = adrian*(times // len(adrian)) + adrian[0:(times%len(adrian))]
bruno = bruno*(times // len(bruno)) + bruno[0:(times%len(bruno))]
goran = goran*(times // len(goran)) + goran[0:(times%len(goran))]

adrian_count = 0
bruno_count = 0
goran_count = 0

for i in range(0,times):
    if text[i] == adrian[i]:
        adrian_count += 1
    
    if text[i] == bruno[i]:
        bruno_count += 1

    if text[i] == goran[i]:
        goran_count += 1

print(max(adrian_count,bruno_count,goran_count))

if adrian_count == bruno_count and bruno_count == goran_count:
    print("Adrian")
    print("Bruno")
    print("Goran")
if adrian_count > bruno_count:
    if adrian_count > goran_count:
        print("Adrian")
    if adrian_count < goran_count:
        print("Goran")
    if adrian_count == goran_count:
        print("Adrian")
        print("Goran")
if bruno_count > adrian_count:
    if bruno_count > goran_count:
        print("Bruno")
    if bruno_count < goran_count:
        print("Goran")
    if bruno_count == goran_count:
        print("Bruno")
        print("Goran")
if adrian_count == bruno_count:
    if adrian_count > goran_count:
        print("Adrian")
        print("Bruno")
    if adrian_count < goran_count:
        print("Goran")
