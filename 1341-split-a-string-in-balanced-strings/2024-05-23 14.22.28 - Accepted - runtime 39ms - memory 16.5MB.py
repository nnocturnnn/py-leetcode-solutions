class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balanced = 0
        count = 0
        for char in s:
            if char == 'R':
                balanced += 1
            elif char == 'L':
                balanced -= 1
            if not balanced:
                count += 1
                balanced = 0
        return count 