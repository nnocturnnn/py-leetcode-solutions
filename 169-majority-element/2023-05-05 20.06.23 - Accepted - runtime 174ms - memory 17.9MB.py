class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cd = {nums.count(i) : i for i in set(nums)}
        return cd[max(cd)]