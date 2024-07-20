class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascals_triangle = []
        for i in range(numRows):
            node = [1] * (i + 1)
            if i > 0:
                for k in range(1, i):
                     node[k] = pascals_triangle[i-1][k-1] + pascals_triangle[i-1][k]
            pascals_triangle.append(node)
        return pascals_triangle
