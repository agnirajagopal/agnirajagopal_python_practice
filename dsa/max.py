def max_element(s):
    current_max=s[0]
    
    for value in s:
        if value>current_max:
            current_max=value
            
    return current_max
s=[1,2,3,4,5]
print(max_element(s))