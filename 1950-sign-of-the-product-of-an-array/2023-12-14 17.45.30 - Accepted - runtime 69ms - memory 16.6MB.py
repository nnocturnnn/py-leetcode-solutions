from functools import reduce

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        out = reduce(lambda x, y: x * y, nums)
        if out > 0:
            return 1
        return -1 if out < 0 else 0