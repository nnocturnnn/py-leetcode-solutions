from itertools import combinations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return combinations(nums, len(nums))