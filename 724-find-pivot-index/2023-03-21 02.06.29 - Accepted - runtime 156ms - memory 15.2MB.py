class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        
        left_sum = 0
        for i in range(len(nums)):
            if left_sum == sum - left_sum - nums[i]:
                return i
            left_sum += nums[i]
        
        return -1