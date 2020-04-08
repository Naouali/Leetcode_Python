#!/usr/bin/python3
def rm_dup(a):
    return list(set(a))

a = [1,2,2,5,6,9,9,14,14,14,17,]
print(rm_dup(a))