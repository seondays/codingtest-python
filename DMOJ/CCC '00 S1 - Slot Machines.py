# https://dmoj.ca/problem/ccc00s1

jar_count = int(input())
first_last_paid = int(input())
second_last_paid = int(input())
third_last_paid = int(input())

machine = 1
playtimes = 0 

while jar_count > 0 :
    jar_count -= 1
    
    if machine == 1 :
        first_last_paid += 1
        
        if first_last_paid == 35 :
            jar_count += 30
            first_last_paid = 0
    
    elif machine == 2 :
        second_last_paid += 1
        
        if second_last_paid == 100 :
            jar_count += 60
            second_last_paid = 0
        
    elif machine == 3 :
        third_last_paid += 1
        
        if third_last_paid == 10 :
            jar_count += 9
            third_last_paid = 0
    
    playtimes += 1
    machine += 1
    
    if machine == 4 :
        machine = 1
    
print("Martha plays", playtimes, "times before going broke.")
    
    
    
        
    

    