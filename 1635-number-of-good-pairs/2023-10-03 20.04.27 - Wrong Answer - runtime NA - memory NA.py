import itertools


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ngp = 0
        for i in range(len(nums)):
            for k in range(i, len(nums)):
                if i == k:
                    ngp += 1
        return ngp


        