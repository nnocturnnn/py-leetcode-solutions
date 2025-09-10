class Solution:
    def judgeCircle(self, moves: str) -> bool:
        coordinate = [0, 0]
        for i in moves:
            if i == "U":
                coordinate[0] += 1
            elif i == "D":
                coordinate[0] -= 1
            elif i == "L":
                coordinate[1] -= 1
            else:
                coordinate[1] += 1
        return coordinate == [0, 0]