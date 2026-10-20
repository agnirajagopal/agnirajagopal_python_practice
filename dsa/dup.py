def return_dup(n):
    dup=[]
    result=[]
    
    for item in n:
        if item in result:
            if item not in dup:
                dup.append(item)
        else:
            result.append(item)
    return result

n=[1,2,3,4,5,1]
print(return_dup(n))