class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column = list(zip(*mat))
        count = 0
        rows = len(mat)
        columns = len(mat[0])

        for i in range(rows):
            for j in range(columns):
                if mat[i][j] == 1 and column[i].count(1) == 1 and mat[j].count(1) == 1:
                    count += 1
        return count