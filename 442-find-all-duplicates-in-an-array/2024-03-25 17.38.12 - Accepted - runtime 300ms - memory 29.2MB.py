class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return Counter(nums)-Counter({*nums})