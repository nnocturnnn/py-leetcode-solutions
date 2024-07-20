class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        substrings = []

        for i in range(n):
            for j in range(i + 1, n + 1):
                substring = s[i:j]
                if substring == substring[::-1]:
                    substrings.append(substring)
        return max(substrings, key=len)