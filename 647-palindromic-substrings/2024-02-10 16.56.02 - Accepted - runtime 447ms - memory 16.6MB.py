class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for start in range(len(s)):
            for end in range(start + 1, len(s) + 1):
                if s[start:end] == s[start:end][::-1]:
                    count += 1
        return count