class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total_sum = sum([mat[i][i] + mat[-i][-i] for i in range(len(mat))])
        if n % 2 == 1:
            total_sum -= mat[n//2][n//2]
        return total_sum