class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        substrings = set()
        n = len(s)
        
        for i in range(n - 1):
            for j in range(i + 1, n):
                ss = s[i:j]
                if n % len(ss) == 0:
                    if ss * (n // len(ss)) == s:
                        return True
        return False
