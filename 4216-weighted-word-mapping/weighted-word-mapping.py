import string
from typing import List

class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        letter_to_weight = dict(zip(string.ascii_lowercase, weights))
        result = []
        for word in words:
            total = sum(letter_to_weight[ch] for ch in word)
            idx = total % 26
            result.append(string.ascii_lowercase[25 - idx])
        return ''.join(result)