class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        result = 0
        result += (28 + 28+7*(weeks-1)) * weeks // 2
        result += (weeks+1 + weeks+1+(days - 1)) * days // 2
        return result