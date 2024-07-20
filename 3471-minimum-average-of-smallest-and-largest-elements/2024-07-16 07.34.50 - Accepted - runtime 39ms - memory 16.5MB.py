import statistics

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        avg = [(nums[i] + nums[-i - 1]) / 2 for i in range(len(nums) // 2)]
        return min(avg)