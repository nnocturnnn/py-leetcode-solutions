from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i, k in edges:
            graph[i].append(k)
            graph[k].append(i)
        
        visited = set()
        def dfs(node):
            visited.add(node)
            if node == destination:
                return True
            for neigh in graph[node]:
                if neigh not in visited:
                    if dfs(neigh):
                        return True
            return False
        return dfs(source)