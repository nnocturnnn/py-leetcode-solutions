from itertools import combinations 

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Sort the array to simplify the computation
        
        closest_sum = float('inf')  # Variable to track the closest sum
        n = len(nums)
        
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                
                if curr_sum == target:
                    return target
                
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest_sum