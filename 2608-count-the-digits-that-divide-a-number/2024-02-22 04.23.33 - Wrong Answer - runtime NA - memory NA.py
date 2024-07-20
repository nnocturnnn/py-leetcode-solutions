class Solution:
    def countDigits(self, num: int) -> int:
        return sum({num : num % 1 == 0 for i in range(1, 10)}.values())