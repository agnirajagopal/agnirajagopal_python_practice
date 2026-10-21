def return_duplicate(n):
    result=''
    dup=""
    for i in n:
        if i in result:
            if i not in dup:
                dup+=i
        else:
            result+=i
            
    return result

n='banana'
print(return_duplicate(n))