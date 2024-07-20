class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        _ = [target.insert(i, num) for num, i in zip(nums, index)]
        return target