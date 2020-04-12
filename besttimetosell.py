#!/usr/bin/python3
def maxprofit(prices):
    minidex = 0
    maxidx = 0
    new = []
    if len (prices) == 0:
        return 0
    if len(prices) ==1:
        return 0
    for i in prices:
        if i != 0:
            new.append(i)
    if min(new) == new[-1]:
        new = new[:-1]
    if max (new) == new[0]:
        new = new[1:]
    for i in range(len(new)):
        if new[i] == min(new):
            minidex = i
            break
    for j in range(len(new)):
        if new[j] == max(new):
            maxidx = j
    print(new)
    if minidex < maxidx:
        return max(new) - min(new)
    return 0



a = [2,1,2,1,0,1,2]
c= [2,1,2,1,0,0,1]
print(maxprofit(a))
#print(maxprofit(c))