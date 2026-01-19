class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        cols_max = [max(col) for col in zip(*matrix)]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == -1:
                    matrix[i][j] = cols_max[j]

        return matrix