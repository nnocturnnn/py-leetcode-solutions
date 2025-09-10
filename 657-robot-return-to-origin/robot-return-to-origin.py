class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coord = [0, 0]
        directions = {"U": (1, 0), "D": (-1, 0), "L": (0, -1), "R": (0, 1)}
        for m in moves:
            dx, dy = directions[m]
            coord[0] += dx
            coord[1] += dy
        return coord == [0, 0]