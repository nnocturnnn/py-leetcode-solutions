
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        start_col, start_row = start[0], int(start[1:])
        end_col, end_row = end[0], int(end[1:])
        
        result = []
        for col in range(ord(start_col), ord(end_col) + 1):
            for row in range(start_row, end_row + 1):
                result.append(f"{chr(col)}{row}")
        return result
