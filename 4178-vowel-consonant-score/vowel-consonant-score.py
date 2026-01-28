class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        vovels = 'aeiou'
        c, v = 0, 0
        for i in s:
            if i.isalpha():
                if i in vovels:
                    v += 1
                else:
                    c += 1
        c = floor(v / c) if c > 0 else 0
        return c