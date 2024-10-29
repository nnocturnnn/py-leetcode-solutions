class Solution:
    def trimMean(self, arr: List[int]) -> float:
        tp = len(arr) * 5 // 100
        arr = sorted(arr)[tp:-tp]
        return sum(arr) / len(arr)
        