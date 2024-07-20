class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        froms = list(set(nums))
        for i in range(len(froms)):
            nums[i] = froms[i]
        return len(froms)