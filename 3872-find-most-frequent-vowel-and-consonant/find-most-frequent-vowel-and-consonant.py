from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:
        counter = Counter(s)
        vowel = "aeiou"
        max_vowel = max((freq for ch, freq in counter.items() if ch in vowel), default=0)
        max_other = max((freq for ch, freq in counter.items() if ch not in vowel), default=0)
        return max_vowel + max_other

        


        