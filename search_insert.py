#!/usr/bin/python3
def searchInsert(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 0
        s= nums
        s.append(target)
        s.sort()
        for i in range(len(s)):
            if s[i] == target:
                return (i)