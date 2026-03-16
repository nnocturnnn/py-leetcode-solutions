class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        left_prefix = [[0]*m for _ in range(n)]
        for j in range(m):
            left_prefix[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(m):
                if j + 1 < m:
                    left_prefix[i][j] = grid[i][j] + left_prefix[i-1][j+1]
                else:
                    left_prefix[i][j] = grid[i][j]

        right_prefix = [[0]*m for _ in range(n)]
        for j in range(m):
            right_prefix[0][j] = grid[0][j]
        for i in range(1, n):
            for j in range(m):
                if j - 1 >= 0:
                    right_prefix[i][j] = grid[i][j] + right_prefix[i-1][j-1]
                else:
                    right_prefix[i][j] = grid[i][j]
        heap = []
        for i in range(n):
            for j in range(m):
                offset = 0
                while j - offset>= 0 and j + offset < m and i + 2*(offset) < n:
                    if offset == 0:
                        temp = grid[i][j]
                    else:
                        temp = left_prefix[i+offset][j-offset] - left_prefix[i][j] + grid[i][j] + right_prefix[i+offset][j+offset] - right_prefix[i][j] + right_prefix[i+2*offset][j]-right_prefix[i+offset][j-offset] + left_prefix[i+2*offset][j] - left_prefix[i+offset][j+offset] - grid[i+2*offset][j]
                    if temp not in heap:
                        heapq.heappush(heap, temp)
                        if len(heap) > 3:
                            heapq.heappop(heap)
                    offset+=1
        heap.sort(key = lambda x: -x)
        return heap