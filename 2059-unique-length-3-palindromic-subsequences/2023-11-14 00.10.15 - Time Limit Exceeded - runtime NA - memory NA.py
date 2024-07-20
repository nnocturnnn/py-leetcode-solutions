import itertools

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return len(set([subs for subs in itertools.combinations(s, 3) if subs == subs[::-1] ]))
        