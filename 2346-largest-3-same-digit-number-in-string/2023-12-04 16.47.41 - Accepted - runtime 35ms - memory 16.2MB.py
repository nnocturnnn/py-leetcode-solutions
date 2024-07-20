class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            threesame = str(i) * 3
            if threesame in num:
                return threesame
        return ""