class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])

        column = list(zip(*grid))
        for i in range(rows):
            ones_row_i = grid[i].count(1)
            zeros_row_i = grid[i].count(0)
            for j in range(cols):
                ones_col_j = column[j].count(1)
                zeros_col_j = column[j].count(0)

                grid[i][j] = ones_row_i + ones_col_j - zeros_row_i - zeros_col_j

        return grid