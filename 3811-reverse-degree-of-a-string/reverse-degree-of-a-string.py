class Solution:
    def reverseDegree(self, s: str) -> int:
        rev_alph = "zyxwvutsrqponmlkjihgfedcba"
        degre = {al : i for i, al in enumerate(rev_alph, start=1)}
        return sum([degre[ch] * i for i, ch in enumerate(s, start=1)])