class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return goal in [s[-i:] + s[:-i] for i in range(len(s))]