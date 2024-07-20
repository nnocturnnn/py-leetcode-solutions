from itertools import chain, combinations

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        all_combinations = chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))
        subsets = [list(combination) for combination in all_combinations]
        return sum(reduce(lambda x, y: x ^ y, ss, 0) for ss in subsets)

