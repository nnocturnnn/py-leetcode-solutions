class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        lnum = len(nums)
        rsum, lsum = [], []
        for i in range(lnum):
            rsum.append(sum(nums[i+1:]))
            lsum.insert(0, sum(nums[:lnum - i - 1]))
        return [abs(l - r) for l, r in zip(lsum, rsum)]
