from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum(len(w) for w in filter(lambda x: not Counter(x) - Counter(chars), words))

            
