class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        position = 0
        max_needl = 0
        for i in moves:
            if i == "R" or i == "_":
                position -= 1
            if i == "L" or i == "-":
                position += 1
            max_needl = max(max_needl, abs(position))
        return max_needl