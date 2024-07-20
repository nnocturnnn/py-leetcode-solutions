class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        return sum([abs(s.index(i) - t.index(i))  for i in s])