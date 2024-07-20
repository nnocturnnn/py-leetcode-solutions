from itertools import combinations_with_replacement

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return combinations_with_replacement(nums, len(nums))