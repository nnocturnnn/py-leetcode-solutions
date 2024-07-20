import math

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid) - 2
        cols = len(grid[0]) - 2
        max_values = []

        for i in range(rows):
            for j in range(cols):
                window = [grid[i + k][j:j + 3] for k in range(3)]
                max_values.append(max(max(row) for row in window))

        return [max_values[i * cols:(i + 1) * cols] for i in range(rows)]