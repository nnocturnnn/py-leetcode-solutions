from collections import Counter

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_counter = Counter(words[0])

        for word in words[1:]:
            common_counter &= Counter(word)

        result = []
        for char, count in common_counter.items():
            result.extend([char] * count)
        
        return result