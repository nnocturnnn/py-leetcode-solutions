class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        return max([y[0] - x[0] for x, y in zip(points, points[1:])])