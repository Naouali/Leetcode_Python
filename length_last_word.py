#!/usr/bin/python3
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        if len(s) < 1:
            return len(s)
        return len(s[-1])