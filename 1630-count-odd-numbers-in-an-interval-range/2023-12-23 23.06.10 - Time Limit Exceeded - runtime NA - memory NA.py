class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return sum(1 for i in range(low, high+1) if i % 2 != 0)