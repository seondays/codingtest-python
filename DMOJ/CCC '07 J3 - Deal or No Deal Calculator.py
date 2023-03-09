#https://dmoj.ca/problem/ccc07j3

money = {"1":100,"2":500,"3":1000,"4":5000,"5":10000,"6":25000,"7":50000,"8":100000,"9":500000,"10":1000000}

open_count = int(input())

for i in range(0,open_count):
    money_number = input()
    money.pop(money_number)

banker_offer = int(input())

left_money = list(money.values())
final_money = 0

for i in left_money:
    final_money += i

if final_money/len(left_money) < banker_offer:
    print("deal")
else:
    print("no deal")