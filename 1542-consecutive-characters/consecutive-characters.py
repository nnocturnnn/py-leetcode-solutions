class Solution:
    def maxPower(self, s: str) -> int:
        prev = s[0]
        count = 1
        maxcount = 1
        for i in range(1,len(s)):
            if s[i] == prev:
                count += 1
            else:
                prev = s[i]
                count = 1
            maxcount = maxcount if maxcount > count else count
        return maxcount
