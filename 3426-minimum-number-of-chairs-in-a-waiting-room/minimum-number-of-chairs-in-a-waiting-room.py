class Solution:
    def minimumChairs(self, s: str) -> int:
        return max(accumulate(map(' E'.find, s)))