from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        inc = Counter(nums)
        return sorted(nums, key=lambda x: (inc[x], -x))