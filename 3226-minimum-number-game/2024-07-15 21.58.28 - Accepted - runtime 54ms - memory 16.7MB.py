class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in range(0, len(nums) - 1, 2):
            arr.append(nums[i + 1])
            arr.append(nums[i])
        if len(nums) % 2 != 0:
            arr += nums[-1]
        return arr
