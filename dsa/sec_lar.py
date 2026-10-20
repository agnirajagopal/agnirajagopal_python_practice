def second_largest(n):
    l=len(n)
    for i in range(l):
        for j in range(i+1,l):
            if n[i]<n[j]:
                n[i],n[j]=n[j],n[i]
    return n[1]

n=[88,44,2,3,4,5]
print(second_largest(n))
    