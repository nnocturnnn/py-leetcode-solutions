class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ite = nums1 if nums1[0] > nums2[0] else nums2
        for i in ite:
            if i in nums1:
                return i
        return -1
