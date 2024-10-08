from itertools import combinations

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        for i in range(len(nums) + 1):
            result.extend(combinations(nums,i))
        return result
        