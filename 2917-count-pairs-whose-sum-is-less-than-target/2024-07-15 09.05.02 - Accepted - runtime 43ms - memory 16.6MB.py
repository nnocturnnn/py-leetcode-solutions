from itertools import combinations

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        return sum([1 for pair in combinations(nums, 2) if sum(pair) < target])