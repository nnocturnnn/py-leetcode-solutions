class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        max_distance = 0
        current_distance = 0
        last_underscore_index = -1

        for i, move in enumerate(moves):
            if move == '_':
                current_distance += 1
                last_underscore_index = i
            else:
                current_distance = i - last_underscore_index

            max_distance = max(max_distance, current_distance)

        return max_distance