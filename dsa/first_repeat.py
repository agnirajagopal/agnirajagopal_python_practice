# def first_repeat(n):
#     dict={}
#     for item in n:
#         if item in dict:
#             dict[item]+=1
#         else:
#             dict[item]=1
            
#     for item in dict:
#         if dict[item]>1:
#             return item
        
# n="abcdefgab"
# print(first_repeat(n))


# def first_non_repeat(n):
#     dict={}
#     for item in n:
#         if item in dict:
#             dict[item]+=1
#         else:
#             dict[item]=1
            
#     for item in dict:
#         if dict[item]==1:
#             return item
        
#     return None

# n="abcdefgab"
# print(first_non_repeat(n))


def second_non_repeat(n):
    dict={}
    for item in n:
        if item in dict:
            dict[item]+=1
        else:
            dict[item]=1
    count=0
    for item in dict:
        if dict[item]==1:
            count+=1
            if count==2:
                return item
        
    return None
n="abcdefgab"
print(second_non_repeat(n))
            
    

        