#https://dmoj.ca/problem/coci17c1p1

cards_count = {2:4,3:4,4:4,5:4,6:4,7:4,8:4,9:4,10:16,11:4}

drawn_count = int(input())
sum_power = 0

for i in range(drawn_count):
    drawn = int(input())
    sum_power += drawn
    cards_count[drawn] = cards_count[drawn]-1

sum_power = 21 - sum_power
lower_power = 0

if sum_power < 11:
    for i in range(2,sum_power+1):
        lower_power += cards_count[i]
        
    higher_power = sum(cards_count.values()) - lower_power

    if lower_power < higher_power :
        print("DOSTA")
    else:
        print("VUCI")

else:
    print("VUCI")




