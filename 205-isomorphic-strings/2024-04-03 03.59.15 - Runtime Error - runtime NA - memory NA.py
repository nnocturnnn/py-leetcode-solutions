class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_map = {}
        used_chars = set()
        for i in range(len(s)):
            if s[i] not in char_map: