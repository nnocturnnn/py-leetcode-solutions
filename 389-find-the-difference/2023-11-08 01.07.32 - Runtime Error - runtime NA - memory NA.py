class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return next(iter(set(t) - set(s)))
        