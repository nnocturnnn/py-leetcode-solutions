import itertools


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return len([i if i[0] == i[1] and i[0] < i[1] else continue for i in itertools.combinations(nums,2)])


        