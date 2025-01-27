from collections import Counter 

class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1, word2 = Counter(word1), Counter(word2)
        all_chars = set(word1.keys()) | set(word2.keys())
        for char in all_chars:
            if abs(word1.get(char, 0) - word2.get(char, 0)) > 3:
                return False
        return True