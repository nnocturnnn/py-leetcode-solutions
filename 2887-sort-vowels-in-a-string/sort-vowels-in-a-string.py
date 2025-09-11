from collections import deque

class Solution:
    def sortVowels(self, s: str) -> str:
        all_vovels = "aeiouAEIOU"
        vowels = deque(sorted([ch for ch in s if ch in all_vovels], key=ord))
        s = list(s)
        for i in range(len(s)):
            if s[i] in all_vovels:
                s[i] = vowels.popleft()
        return "".join(s)