class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) < 5:
            return 0
        else:
            print([nums[i] - nums[i + 3] for i in range(len(nums) - 4)])
        return 1
