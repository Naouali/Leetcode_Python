#!/usr/bin/python3
def trail(n):
    facto = 1
    value = 0
    for i in range(1, n+1):
        facto = facto * i
    print(facto)
    while facto:
        rem = facto %  10
        facto = facto // 10
        if rem != 0:
            break
        if rem == 0:
            value += 1
    return value


print(trail(7317))