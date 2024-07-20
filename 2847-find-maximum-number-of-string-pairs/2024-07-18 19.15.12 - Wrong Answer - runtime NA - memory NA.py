class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        def sum_of_ascii(s: str) -> int:
            return sum(ord(char) for char in s)
        return len(words) - len(set([sum_of_ascii(i) for i in words])) 