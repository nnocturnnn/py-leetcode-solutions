class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        position = 0
        furthest_distance = 0

        for move in moves:
            if move == 'L' or move == '_':
                position -= 1
            if move == 'R' or move == '_':
                position += 1
            furthest_distance = max(furthest_distance, abs(position))

        return furthest_distance