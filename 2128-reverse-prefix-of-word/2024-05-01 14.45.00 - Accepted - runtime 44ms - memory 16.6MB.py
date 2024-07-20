class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        prefix = word[0:word.index(ch) + 1]
        return word.replace(prefix,prefix[::-1])