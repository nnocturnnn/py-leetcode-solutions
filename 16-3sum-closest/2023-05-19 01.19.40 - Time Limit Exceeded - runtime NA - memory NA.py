from itertools import combinations 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return min([sum(i) for i in combinations(nums, 3)], key=lambda x:abs(x-target))