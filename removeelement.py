#!/usr/bin/python3
def _remove(a,n):
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] == n:
                a[j] = a[j+1]
    return a


print(_remove([1,1,2,5,6,7,1],1))