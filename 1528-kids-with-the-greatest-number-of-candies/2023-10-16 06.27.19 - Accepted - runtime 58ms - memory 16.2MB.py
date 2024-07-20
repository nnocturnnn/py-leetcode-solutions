class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if all(i + extraCandies >= element for element in candies) else False for i in candies]