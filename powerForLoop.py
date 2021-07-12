def power (base_num, pow_num):
    result = 1
    for x in range(pow_num):        #range() - number of loops starting zero
        result = result * base_num
        #print(x)         - to show number of loops
    return result

print(power(2,3))