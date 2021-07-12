def get_middle(s):
    #your code here
    if len(s) % 2 == 0:
        a = len(s) / 2
        mid1 = s[int(a) -1] 
        mid2 = s[int(a)]
        mid = mid1 + mid2 
    else:
        b = len(s) / 2
        mid =  s[int(b)]
    return mid

print(get_middle("Have a good day"))