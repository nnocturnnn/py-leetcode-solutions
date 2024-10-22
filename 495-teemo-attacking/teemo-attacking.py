class Solution:
    def findPoisonedDuration(self, ts: List[int], duration: int) -> int:
        return sum([duration if (ts[i + 1] - ts[i]) > duration else (ts[i + 1] - ts[i]) for i in range(len(ts) - 1)]) + duration