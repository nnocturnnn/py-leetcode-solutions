class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        lst = [nums[i-1] + nums[i] + nums[i+1] for i in range(1, len(nums) - 1)]
        print(lst)
        return min(lst, key=lambda x:abs(x-target))