# https://dmoj.ca/problem/dmopc14c7p2

maesure_count = int(input())
maesure_values = [int(i) for i in input().split(" ")]

minimum_index = maesure_values.index(min(maesure_values))
minimum_values = min(maesure_values)
unknown = False

print(len(maesure_values))

if minimum_index == len(maesure_values)-1:
    unknown = True

for i in range(minimum_index+1,len(maesure_values)):

    if maesure_values[i] < minimum_values:
        if minimum_values == max(maesure_values):
            break
        unknown = True
        break
    else:
        minimum_values = maesure_values[i]

if unknown == True:
    print("unknown")
if unknown == False:
    print(minimum_values-min(maesure_values))



