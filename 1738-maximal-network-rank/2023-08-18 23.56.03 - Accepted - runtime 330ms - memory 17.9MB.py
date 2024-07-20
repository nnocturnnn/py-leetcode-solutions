class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        
        for road in roads:
            u, v = road
            graph[u].append(v)
            graph[v].append(u)
        
        max_rank = 0
        
        for i in range(n):
            for j in range(i + 1, n):
                rank = len(graph[i]) + len(graph[j])
                if j in graph[i] or i in graph[j]:
                    rank -= 1
                
                max_rank = max(max_rank, rank)
        
        return max_rank