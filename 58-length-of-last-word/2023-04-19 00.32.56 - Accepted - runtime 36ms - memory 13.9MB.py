class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(list(map(str.strip, s.split()))[-1])