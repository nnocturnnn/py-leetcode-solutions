class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        max_values = []

        for i in range(rows - 2):
            for j in range(cols - 2):
                window = [grid[i + k][j:j + 3] for k in range(3)]
                max_values.append(max(max(row) for row in window))

        return [array[i * cols:(i + 1) * cols] for i in range(rows)]