class Solution:
    def countDigits(self, num: int) -> int:
        nums = str(num)
        return sum([1 if num % int(i) == 0 else 0 for i in nums])