class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        nz = 0
        i = len(num) - 1
        while i >= 0 and num[i] == '0':
            i -= 1
            nz -= 1
        if not nz:
            return num
        return num[0:nz]