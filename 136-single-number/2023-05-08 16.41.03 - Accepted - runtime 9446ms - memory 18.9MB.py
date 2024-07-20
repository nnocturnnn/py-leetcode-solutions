class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts_items = {nums.count(i) : i for i in nums}
        return counts_items[min(counts_items)]