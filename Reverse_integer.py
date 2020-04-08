class Solution:
    def reverse(self, x: int) -> int:
        if type(x) != int:
            return 0
        if x <= -2**31-1 or x >= 2** 31 -1:
            return 0
        z = 0
        if x < 0:
           z = 1
           x = -x
        count = 0
        k = x
        while k > 0:
            r = k % 10
            k = k // 10
            count += 1

        value = 10 ** count
        res = 0
        while x > 0:
            rem = x % 10
            x = x // 10
            res += rem * value
            value = value // 10
        if z == 1:
            return res * -1 // 10
        return res // 10
        
