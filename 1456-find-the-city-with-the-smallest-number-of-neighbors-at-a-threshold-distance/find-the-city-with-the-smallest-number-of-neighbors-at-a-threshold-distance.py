from collections import defaultdict

class Solution:
    def dijkstra(self, graph, start):
        priority_queue = [(0, start)]
        shortest_paths = {node: float('inf') for node in graph}
        shortest_paths[start] = 0
        previous_nodes = {node: None for node in graph}
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            if current_distance > shortest_paths[current_node]:
                continue
            for neighbor, weight in graph[current_node]:
                distance = current_distance + weight
                if distance < shortest_paths[neighbor]:
                    shortest_paths[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        return shortest_paths

    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for fcity, scity, weight in edges:
            graph[fcity].append((scity, weight))
            graph[scity].append((fcity, weight))
        
        shortestPathMatrix = [[0] * n for _ in range(n)]

        for i in range(n):
            shortest_paths = self.dijkstra(graph, i)
            for j in range(n):
                shortestPathMatrix[i][j] = shortest_paths.get(j, float('inf'))

        count = {}
        for i in range(n):
            key = len(list(filter(lambda x: x <= distanceThreshold,
                shortestPathMatrix[i]))) - 1
            if key in count:
                if count[key] < i:
                    count[key] = i
            else:
                count[key] = i
        return count[min(count.keys())]