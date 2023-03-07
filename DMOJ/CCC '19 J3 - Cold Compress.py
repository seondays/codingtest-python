#https://dmoj.ca/problem/ccc19j3

count = int(input())

for i in range(0,count):
    
    sentence = input()
    list = []
    same_count = 0
    save = sentence[0]

    for i in sentence:
        
        if i == save :
            same_count += 1
        
        else:
            list.append(same_count)
            list.append(save)
            same_count = 1
        
        save = i
        
    list.append(same_count)
    list.append(save)
    
    for i in list:
        print(i,end=" ")
    print("\n")