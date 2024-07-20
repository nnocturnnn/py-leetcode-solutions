class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return True if any([word.capitalize() == word, word.isupper(), word.islower()]) else False