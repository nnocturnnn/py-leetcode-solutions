class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        return [list(s) for s in [set(nums1) - set(nums2), set(nums2) - set(nums1)]]