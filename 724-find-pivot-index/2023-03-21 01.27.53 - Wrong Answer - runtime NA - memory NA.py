class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(1,len(nums)):
            if sum(nums[:i+1]) == sum(nums[i+2:]):
                return i + 1
        if sum(nums[1:]) == 0 or sum(nums[:-1]) == 0:
            return 0
        return -1