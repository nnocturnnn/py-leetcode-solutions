class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                for k in range(n - 1,i,-1):
                    if nums[k] != 0:
                        nums[i], nums[k] = nums[k], nums[i]

        