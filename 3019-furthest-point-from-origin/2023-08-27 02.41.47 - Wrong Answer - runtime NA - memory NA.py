class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        left_count = 0
        right_count = 0
        max_distance = 0

        for move in moves:
            if move == 'L':
                left_count += 1
                right_count = 0
            elif move == 'R':
                right_count += 1
                left_count = 0
            else:
                left_count += 1
                right_count += 1

            max_distance = max(max_distance, left_count, right_count)

        return max_distance - 1