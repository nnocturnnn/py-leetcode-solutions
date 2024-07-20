class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * rows for i in range(cols)]
        for i in range(rows):
            for k in range(cols):
                m = min(rowSum[i],colSum[k])
                if m > 0:
                    matrix[i][k] = m
                    rowSum[i] -= m
                    colSum[k] -= m
                else:
                    matrix[i][k] = 0
        return matrix 