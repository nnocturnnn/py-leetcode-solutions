class Solution:
    def maxScore(self, s: str) -> int:
        return max([s[0:i].count("0") + s[i:-1].count("1") for i in range(1, len(s) - 1)])
