# https://dmoj.ca/problem/wc17c3j3

id = str(input())

def check_lowercase(id) :
    
    count = 0
    
    for i in id :
        if i.islower() :
            count += 1
    
    return count >= 3

def check_uppercase(id) :
    
    count = 0
    
    for i in id :
        if i.isupper() :
            count += 1
    
    return count >= 2

def check_digit(id) :
    
    count = 0
    
    for i in id :
        if i.isdigit() :
            count += 1
            
    return count >= 1

def check_length(id) :
    
    if len(id) >= 8 and len(id) <= 12 :
        return True
    else :
        return False

if check_digit(id) and check_length(id) and check_lowercase(id) and check_uppercase(id) :
    print("Valid")
else :
    print("Invalid")
