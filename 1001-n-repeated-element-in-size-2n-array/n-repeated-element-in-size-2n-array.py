class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        d = Counter(nums)
        for x in d:
            if d[x] == len(nums)//2:
                return x