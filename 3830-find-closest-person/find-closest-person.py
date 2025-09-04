class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        f, s = abs(x - z), abs(y - z)
        return 1 if f < s else 2 if f > s else 0