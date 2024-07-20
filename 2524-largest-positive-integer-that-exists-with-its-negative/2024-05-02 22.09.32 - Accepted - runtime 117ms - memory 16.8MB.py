class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in nums:
            if (i * -1) in nums:
                return i 
        return -1