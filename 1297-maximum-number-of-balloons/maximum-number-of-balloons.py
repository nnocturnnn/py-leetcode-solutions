from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        required_chars = {
            'b': 1,
            'a': 1,
            'l': 2,
            'o': 2,
            'n': 1
        }
        
        return min(count[char] // required_chars[char] for char in required_chars)