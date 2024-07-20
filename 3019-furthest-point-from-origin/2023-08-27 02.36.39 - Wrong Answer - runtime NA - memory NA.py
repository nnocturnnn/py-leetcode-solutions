class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        position = 0
        max_distance = 0

        for move in moves:
            if move == 'L' or move == '_':
                position -= 1
            if move == 'R' or move == '_':
                position += 1
            max_distance = max(max_distance, abs(position))

        return max_distance
        