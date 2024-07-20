import math

class Solution:
    def merge_sorted_arrays(self, arr1, arr2):
        i = j = 0
        merged = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                merged.append(arr1[i])
                i += 1
            else:
                merged.append(arr2[j])
                j += 1
        merged += arr1[i:]
        merged += arr2[j:]
        return merged

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge_arr = self.merge_sorted_arrays(nums1,nums2)
        len_arr = len(merge_arr) - 1
        return merge_arr[math.ceil(len_arr / 2)]  if len_arr % 2 == 0 else (merge_arr[int(len_arr / 2)] + merge_arr[int(len_arr / 2 + 1)]) / 2
