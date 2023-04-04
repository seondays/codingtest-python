#https://dmoj.ca/problem/ecoo15r1p1

for i in range(10):

    smarties_list= [0,0,0,0,0,0,0,0]
    input_smarties = ''
    time = 0

    while input_smarties != 'end of box':
        input_smarties = input()
        
        if input_smarties == 'orange':
            smarties_list[0] += 1
        if input_smarties == 'blue':
            smarties_list[1] += 1
        if input_smarties == 'green':
            smarties_list[2] += 1
        if input_smarties == 'yellow':
            smarties_list[3] += 1
        if input_smarties == 'pink':
            smarties_list[4] += 1
        if input_smarties == 'violet':
            smarties_list[5] += 1
        if input_smarties == 'brown':
            smarties_list[6] += 1
        if input_smarties == 'red':
            smarties_list[7] += 1

    for i in range(len(smarties_list)):
        
        if i == 7 :
            time += smarties_list[i] * 16
            break
        
        if smarties_list[i] <= 7 :
            time += 13
        
        if smarties_list[i] > 7:
            
            if smarties_list[i] % 7 != 0:
                time += 13
                
            time += (smarties_list[i]//7) * 13

    print(time)