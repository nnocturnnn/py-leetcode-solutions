import re

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        numbers = {int(num) for num in re.findall(r"\d+", word)}
        return len(set(numbers))