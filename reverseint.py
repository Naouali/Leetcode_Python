#!/usr/bin/python3
def rev(x):
    z = 0
    if x < 0:
       z = 1
       x = -x
    count = 0
    k = x
    while k > 0:
        r = k % 10
        k = k // 10
        count += 1
    
    value = 10 ** count
    res = 0
    while x > 0:
        rem = x % 10
        x = x // 10
        res += rem * value
        value = value // 10
    if z == 1:
        return res * -1 // 10
    return res // 10
print(rev(159698))
print(rev(65))
print(rev(31))
print(rev(-951))
print(rev(-9514258))
print(rev(120))
