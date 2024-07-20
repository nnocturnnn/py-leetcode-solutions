class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff = set([nums[i] - nums[i + 1] for i in range(len(nums) - 1)])
        return True if (len(diff) == 2 and 0 in diff) or len(diff) == 1 else False
        