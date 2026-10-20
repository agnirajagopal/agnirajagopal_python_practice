def first_repeat(n):
    dict={}
    for item in n:
        if item in dict:
            dict[item]+=1
        else:
            dict[item]=1
            
    for item in dict:
        if dict[item]>1:
            return item
        
n="abcdefgab"
print(first_repeat(n))

        