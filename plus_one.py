#!/usr/bin/python3
def plus(a):
    my = []
    for i in range(len(a)):
        if i == len(a) - 1:
            my.append(a[len(a)-1]+1)
        else:
            my.append(a[i])
    return my

print(plus([1,2,4,5]))