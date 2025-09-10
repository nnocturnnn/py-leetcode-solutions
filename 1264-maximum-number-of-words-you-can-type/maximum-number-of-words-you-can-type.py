class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        i = 0
        for word in text.split():
            if not set(word) & set(brokenLetters):
                i += 1
        return i