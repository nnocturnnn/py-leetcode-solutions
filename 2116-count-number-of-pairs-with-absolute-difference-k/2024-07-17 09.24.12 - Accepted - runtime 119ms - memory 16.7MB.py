from itertools import combinations

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        return sum([1 for i, j in combinations(nums, 2) if abs(i - j) == k])