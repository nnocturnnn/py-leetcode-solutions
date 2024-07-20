from collections import Counter
from functools import reduce

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        twice = [key for key, val in Counter(nums).items() if val == 2]
        if twice:
            return reduce(lambda x, y: x ^ y, twice)
        return 0