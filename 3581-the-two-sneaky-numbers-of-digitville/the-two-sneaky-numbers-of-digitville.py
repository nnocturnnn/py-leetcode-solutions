class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            if nums.count(nums[i]) > 1 and nums[i] not in result:
                result.append(nums[i])
        return result
            