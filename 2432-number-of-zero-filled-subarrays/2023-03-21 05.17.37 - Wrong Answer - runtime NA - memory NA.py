from collections import defaultdict

class Solution:
            
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1
        cum_sum = 0
        for num in nums:
            cum_sum += num
            count += prefix_sums[cum_sum]
            prefix_sums[cum_sum] += 1
        return count