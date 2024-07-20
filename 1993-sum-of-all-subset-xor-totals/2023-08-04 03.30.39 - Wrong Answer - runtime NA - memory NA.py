from itertools import chain, combinations

class Solution:
    XOR = lambda x, y: x ^ y
    
    def subsetXORSum(self, nums: List[int]) -> int:
        all_combinations = chain.from_iterable(combinations(nums, r) for r in range(1, len(nums) + 1))
        subsets = [set(combination) for combination in all_combinations]
        return sum([reduce(Solution.XOR, ss) for ss in subsets])

