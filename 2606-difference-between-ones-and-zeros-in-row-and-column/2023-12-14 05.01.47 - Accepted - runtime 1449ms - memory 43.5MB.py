class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        ones_row = [0] * rows
        zeros_row = [0] * rows
        ones_col = [0] * cols
        zeros_col = [0] * cols

        for i in range(rows):
            for j in range(cols):
                ones_row[i] += grid[i][j]
                zeros_row[i] += 1 - grid[i][j]
                ones_col[j] += grid[i][j]
                zeros_col[j] += 1 - grid[i][j]

        for i in range(rows):
            for j in range(cols):
                grid[i][j] = ones_row[i] + ones_col[j] - zeros_row[i] - zeros_col[j]

        return grid