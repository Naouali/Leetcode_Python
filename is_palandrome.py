class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = 0
        m = x
        s = 1
        if x < 0:
            s = -1
        while x > 0:
            rem = x % 10
            x = x // 10
            res = res *10 + rem * s
        res = res * s
        if res == m or res == m * -1:
            return True
        else:
            return False