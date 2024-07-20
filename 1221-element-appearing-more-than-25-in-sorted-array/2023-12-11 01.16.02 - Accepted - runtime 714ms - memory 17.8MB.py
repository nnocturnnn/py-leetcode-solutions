class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return next(i for i in arr if arr.count(i) / len(arr) > 0.25)