class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        return sum(nums) - sum(int(digit) for num in nums for digit in str(num)) 