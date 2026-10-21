def reverse_number(n):
    m=n
    result=0
    while m!=0:
        l_d=m%10
        result=result*10+l_d
        m//=10
    return result

n=1234
print(reverse_number(n))

def count_number(n):
    count=0
    
    while n>0:
        count+=1
        n=n//10
        
    return count

n=12345 
print(count_number(n))
        