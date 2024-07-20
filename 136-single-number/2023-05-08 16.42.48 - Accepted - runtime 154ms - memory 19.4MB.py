from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return min(counts, key=counts.get)