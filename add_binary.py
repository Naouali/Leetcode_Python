#!/usr/bin/python3
def addBinary(a,b):
    a = int(a,2)
    b = int(b,2)
    binary = bin(a+b)
    return binary[2:]