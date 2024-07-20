class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        column = list(zip(*mat))
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1 and sum(column[i]) == 1 and sum(mat[j]) == 1:
                    print(f"Cell ({i}, {j})")
                    count += 1
        return count