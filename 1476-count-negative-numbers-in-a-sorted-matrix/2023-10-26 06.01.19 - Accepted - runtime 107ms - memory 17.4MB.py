class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def countNegativesInRow(row):
            left, right = 0, len(row) - 1
            count = 0

            while left <= right:
                mid = left + (right - left) // 2

                if row[mid] < 0:
                    count += right - mid + 1
                    right = mid - 1
                else:
                    left = mid + 1

            return count

        total_count = 0

        for row in grid:
            total_count += countNegativesInRow(row)

        return total_count
        