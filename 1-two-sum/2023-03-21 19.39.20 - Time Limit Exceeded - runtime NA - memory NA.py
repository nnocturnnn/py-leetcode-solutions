from itertools import combinations
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        all_combinations = dict()
        for comb, ind in zip(combinations(nums, 2), list(combinations(range(len(nums)), 2))):
            all_combinations[sum(comb)] = ind
        return all_combinations[target]