class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(i - t.index(k))  for i, k in enumerate(s)])