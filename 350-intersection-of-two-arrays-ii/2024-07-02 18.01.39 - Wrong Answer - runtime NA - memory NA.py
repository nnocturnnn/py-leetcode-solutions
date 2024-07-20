class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [value for value in nums1 if value in nums2]