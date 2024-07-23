from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int: 
        if n == 1: return 1
        trusting_visited = set()
        trusted_count = defaultdict(int)
        possible_judge = []

        for trusting, trusted in trust:
            trusting_visited.add(trusting)
            trusted_count[trusted] += 1
            if trusted_count[trusted] == n - 1:
                possible_judge.append(trusted)
        
        for cand in possible_judge:
            if cand in trusting_visited:
                return -1
            
        return possible_judge[0] if possible_judge else -1