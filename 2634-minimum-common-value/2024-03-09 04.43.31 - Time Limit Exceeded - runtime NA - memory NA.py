class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ite, finder = (nums1, nums2) if nums1[0] > nums2[0] else (nums2, nums1)
        for i in ite:
            if i in finder:
                return i
        return -1

