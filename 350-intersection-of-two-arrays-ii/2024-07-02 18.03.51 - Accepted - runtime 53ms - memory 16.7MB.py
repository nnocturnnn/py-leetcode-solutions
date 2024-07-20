class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        for value in nums1:
            if value in nums2:
                out.append(value)
                nums2.remove(value)
        return out