class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        position = 0
        max_distance = 0
        last_underscore_index = -1

        for i, move in enumerate(moves):
            if move == 'L':
                position -= 1
            if move == 'R':
                position += 1
            if move == '_':
                last_underscore_index = i
            max_distance = max(max_distance, abs(position - last_underscore_index))

        return max_distance
        