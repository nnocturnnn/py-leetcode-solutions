class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        mnums = max(nums)
        for i in range(0, mnums):
            if i not in nums:
                return i
        return mnums + 1