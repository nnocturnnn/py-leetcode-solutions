class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        depth = 0
        for i in s:
            if i == '(':
                depth += 1
                max_depth = depth if depth > max_depth else max_depth
            elif i == ')':
                depth -= 1
        return max_depth
