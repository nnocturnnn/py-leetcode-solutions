class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        ncandy = len(candyType) // 2
        return min(len(set(candyType)), ncandy)