class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_sq = 0
        n = len(arr)
        for i in range(n):
            for j in range(i, n):
                sum_sq += pow(len(set(arr[i:j+1])),2)
        return sum_sq