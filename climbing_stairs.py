#!/usr/bin/python3
def staire(n):
    step = n
    value = 0
    while n > 0:
        n = n - 2
        if n < 0:
            break
        value += 1
    return value + step 

print(staire(3))
print(staire(3)) 

