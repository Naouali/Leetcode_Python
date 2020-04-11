#!/usr/bin/python3
def mypow(x, n):
    l = n
    if n < 0:
        n *= -1
    if n == 0:
        return 1
    i = 0
    m = 1
    while i < n:
        m = m * x
        i += 1
    if l < 0:
        return 1/m 
    return m

