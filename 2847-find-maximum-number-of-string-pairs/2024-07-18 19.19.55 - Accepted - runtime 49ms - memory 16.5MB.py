class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        return sum(v[::-1] in words[i+1:] for i,v in enumerate(words))