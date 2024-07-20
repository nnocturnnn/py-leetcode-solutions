class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        l_nums1 = len(nums1)
        for i in reversed(range(l_nums1)):
            if n == 0 or m == 0:
                break
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[i] = nums1[m - 1]
                m -= 1
            else:
                nums1[i] = nums2[n - 1]
                n -= 1

            
        
        