class Solution:
    from collections import defaultdict, deque

    def topological_sort(self, n, conditions):
        graph = defaultdict(list)
        indegree = {i: 0 for i in range(1, n + 1)}

        for u, v in conditions:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque([node for node in indegree if indegree[node] == 0])
        sorted_order = []

        while queue:
            node = queue.popleft()
            sorted_order.append(node)
            for neighbor in graph[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(sorted_order) == n:
            return sorted_order
        else:
            return []

    def buildMatrix(self, k, rowConditions, colConditions):
        row_order = self.topological_sort(k, rowConditions)
        col_order = self.topological_sort(k, colConditions)

        if not row_order or not col_order:
            return []

        row_pos = {num: i for i, num in enumerate(row_order)}
        col_pos = {num: i for i, num in enumerate(col_order)}

        matrix = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            matrix[row_pos[num]][col_pos[num]] = num

        return matrix
            