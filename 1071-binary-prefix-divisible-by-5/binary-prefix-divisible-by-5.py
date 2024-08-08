from itertools import accumulate 

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        return [x == 0 for x in accumulate(nums, lambda x, y: (2*x+y)%5)]