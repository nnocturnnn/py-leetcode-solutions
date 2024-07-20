class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return sum([len(word) if set(word).issubset(set(chars)) else 0 for word in words])
            
