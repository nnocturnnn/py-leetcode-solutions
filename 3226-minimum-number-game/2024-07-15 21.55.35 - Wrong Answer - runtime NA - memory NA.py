class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        arr = []
        nums.sort()
        for i in range(len(nums) // 2 + 1):
            arr.append(nums[i])
            if i != len(nums) - i - 1:
                arr.append(nums[len(nums) - i - 1])
        return arr