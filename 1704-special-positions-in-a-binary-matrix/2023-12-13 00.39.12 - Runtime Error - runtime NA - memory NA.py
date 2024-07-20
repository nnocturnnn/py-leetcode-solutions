class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column = list(zip(*mat))
        count = 0
        print(column)
        for i in range(len(mat)):
            for j in range(len(mat)):
                if mat[i][j] == 1 and column[j].count(1) == 1 and mat[i].count(1) == 1:
                    count += 1
        return count