class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        n = len(nums)
        left, right = 0, nums[n - 1] - nums[0]
        
        while left < right:
            mid = (left + right) // 2
            count = 0
            j = 0
            
            for i in range(n):
                while j < n and nums[j] <= nums[i] + mid:
                    j += 1
                count += j - i - 1
            
            if count < p:
                left = mid + 1
            else:
                right = mid
        
        return left