class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return int(k*nums[-1] + (k*(k-1))/2);    
        