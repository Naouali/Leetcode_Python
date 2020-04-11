#!/usr/bin/python3
def removeElement(nums, val):
        count = 0
        inc = 0
        for i in range(len(nums)):
            for j in range(len(nums)-1):
                if nums[j] == val:
                    temp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = temp
        for x in nums:
            if x == val:
                count+=1
        print(count)
        print(nums)
        while inc < count:
            nums.pop()
            inc += 1
        return nums


b= [2,2,3]
print(removeElement(b,2))
