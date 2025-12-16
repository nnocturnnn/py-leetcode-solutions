class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        return sorted(list(set(nums) ^ set(range(min(nums), max(nums) + 1))))
        
        