class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        diff = (set(t) - set(s))
        return diff.pop() if diff else ""
        