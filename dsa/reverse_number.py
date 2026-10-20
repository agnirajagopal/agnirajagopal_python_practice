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