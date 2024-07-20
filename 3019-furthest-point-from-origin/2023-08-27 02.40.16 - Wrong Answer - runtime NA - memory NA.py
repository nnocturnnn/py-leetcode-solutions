class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        max_distance = 0
        current_distance = 0

        for move in moves:
            if move == '_':
                current_distance += 1
            else:
                current_distance = 0

            max_distance = max(max_distance, current_distance)

        return max_distance