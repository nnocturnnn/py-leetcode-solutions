from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return "".join([fl + sl for fl, sl in zip_longest(word1, word2, fillvalue="")])

            