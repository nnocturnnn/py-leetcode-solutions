class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        sorted_arr = sorted(nums, reverse=True)
        return (sorted_arr[0] - 1) * (sorted_arr[1] - 1)