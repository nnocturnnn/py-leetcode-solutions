from itertools import combinations

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        return sum([1 for i, j, k in combinations([i for i in range(len(nums))], 3) if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff])