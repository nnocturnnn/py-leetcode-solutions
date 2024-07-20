class Solution:
    def largestOddNumber(self, num: str) -> str:
        length = len(num)
        for i in range(length, 0, -1):
            for j in range(length - i + 1):
                ss = num[j:j+i]
                if int(ss) % 2 != 0:
                    return ss
        return ""